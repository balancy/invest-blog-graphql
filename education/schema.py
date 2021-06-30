from django.contrib.auth.models import User

import graphene
from graphene_django import DjangoObjectType

from education.models import (
    Category, 
    Course, 
    Mentor, 
    Student, 
    )


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "username", "is_staff")


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "title", "courses")


class MentorType(DjangoObjectType):
    class Meta:
        model = Mentor
        fields = ("id", "status", "user")


class CourseType(DjangoObjectType):
    class Meta:
        model = Course
        fields = ("id", "category", "title", "students", "mentors")


class StudentType(DjangoObjectType):
    class Meta:
        model = Student
        fields = ("id", "status", "user")


class Query(graphene.ObjectType):
    all_categories = graphene.List(CategoryType)
    category_by_title = graphene.List(
        CategoryType, 
        title=graphene.String(required=True),
    )
    
    def resolve_all_categories(root, info):
        return Category.objects.prefetch_related("courses").all()

    def resolve_category_by_title(root, info, title=None):
        categories = Category.objects.all()
        if title:
            return categories.filter(title__contains=title)


class CreateCategory(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        title = graphene.String(required=True)
        id = graphene.ID()

    # The class attributes define the response of the mutation
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, title):
        category = Category.objects.create(title=title)
        # Notice we return an instance of this mutation
        return CreateCategory(category=category)


class CreateCategoryMutation(graphene.ObjectType):
    create_category = CreateCategory.Field()


schema = graphene.Schema(query=Query, mutation=CreateCategoryMutation)