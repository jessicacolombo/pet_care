from rest_framework.views import APIView, Request, Response, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from pets.models import Pet
from traits.models import Trait
from groups.models import Group
from pets.serializers import PetSerializer
from django.shortcuts import get_object_or_404


# Create your views here.
class PetsViews(APIView, PageNumberPagination):
    def post(self, request: Request) -> Response:
        serializer = PetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        group = serializer.validated_data.pop("group")
        traits_list = serializer.validated_data.pop("traits")

        group_obj = Group.objects.filter(
            scientific_name__iexact=group["scientific_name"]
        ).first()

        if not group_obj:
            group_obj = Group.objects.create(**group)

        new_pet = Pet.objects.create(**serializer.validated_data, group=group_obj)

        for trait in traits_list:
            trait_obj = Trait.objects.filter(name__iexact=trait["name"]).first()

            if not trait_obj:
                trait_obj = Trait.objects.create(**trait)

            new_pet.traits.add(trait_obj)

        serializer = PetSerializer(new_pet)

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        trait_filter = request.query_params.get("trait", None)

        if trait_filter:
            trait = get_object_or_404(Trait, name=trait_filter)

            pets = Pet.objects.filter(traits=trait.id).order_by("id")
        else:
            pets = Pet.objects.get_queryset().order_by("id")

        result_page = self.paginate_queryset(pets, request, view=self)
        serializer = PetSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)


class PetsComposedViews(APIView):
    def get(self, request: Request, pet_id: int) -> Response:
        pet = get_object_or_404(Pet, id=pet_id)
        serializer = PetSerializer(pet)

        return Response(serializer.data)

    def patch(self, request: Request, pet_id: int) -> Response:
        pet = get_object_or_404(Pet, id=pet_id)

        serializer = PetSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        traits = serializer.validated_data.pop("traits", None)
        group = serializer.validated_data.pop("group", None)

        if traits:
            pet.traits.clear()

            for trait in traits:
                trait_obj = Trait.objects.filter(name__iexact=trait["name"]).first()

                if not trait_obj:
                    trait_obj = Trait.objects.create(**trait)

                pet.traits.add(trait_obj)

        if group:
            group_obj = Group.objects.filter(
                scientific_name__iexact=group["scientific_name"]
            ).first()

            if not group_obj:
                group_obj = Group.objects.create(**group)

            pet.group = group_obj

        for key, value in serializer.validated_data.items():
            setattr(pet, key, value)

        pet.save()
        serializer = PetSerializer(pet)

        return Response(serializer.data)

    def delete(self, request: Request, pet_id: int) -> Response:
        pet = get_object_or_404(Pet, id=pet_id)
        pet.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
