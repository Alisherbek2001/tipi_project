from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import CustomUser
from common.permissions import IsSuperAdmin
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class CreateUserView(APIView):
    permission_classes = [IsAuthenticated, IsSuperAdmin]

    def post(self, request):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")
        role = request.data.get("role")

        if not username or not email or not password or not role:
            return Response(
                {"error": "Barcha maydonlar talab qilinadi."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if role not in ["ADMIN", "SUPER_ADMIN"]:
            return Response(
                {"error": "Faqat ADMIN yoki SUPER_ADMIN roliga ruxsat berilgan."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            user = CustomUser.objects.create_user(
                username=username, email=email, password=password, role=role
            )
            return Response(
                {
                    "message": f"Foydalanuvchi yaratildi: {user.username}",
                    "role": user.role,
                    "password": password,
                },
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        confirm_new_password = request.data.get("confirm_new_password")

        if not old_password or not new_password or not confirm_new_password:
            return Response(
                {"error": "Hamma maydon talab qilinadi."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if new_password != confirm_new_password:
            return Response({"error": "Yangi password bir biriga mos kelmadi"})

        if not user.check_password(old_password):
            return Response(
                {"error": "Eski parol noto'g'ri."}, status=status.HTTP_400_BAD_REQUEST
            )

        user.set_password(new_password)
        user.save()

        return Response(
            {"message": "Parol muvaffaqiyatli yangilandi."}, status=status.HTTP_200_OK
        )


class AdminsListAPIView(APIView):
    permission_classes = [IsAuthenticated, IsSuperAdmin]

    def get(self, request):
        admins = CustomUser.objects.all()
        admins_data = [
            {
                "id": admin.id,
                "username": admin.username,
                "email": admin.email,
                "full_name": (
                    admin.get_full_name()
                    if hasattr(admin, "get_full_name")
                    else f"{admin.first_name} {admin.last_name}"
                ),
                "is_active": admin.is_active,
                "role": admin.role,
            }
            for admin in admins
        ]
        return Response(admins_data, status=status.HTTP_200_OK)


class DeleteUserAPIView(APIView):
    permission_classes = [IsAuthenticated, IsSuperAdmin]

    def delete(self, request, user_id=None):
        try:
            if user_id == request.user.id:
                return Response(
                    {"error": "You cannot delete yourself."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            user = CustomUser.objects.get(id=user_id)
            # if user.role == "SUPER_ADMIN":
            #     return Response(
            #         {"error": "You cannot delete SUPER_ADMIN"},
            #         status=status.HTTP_400_BAD_REQUEST,
            #     )

            user.delete()

            return Response(
                {"message": f"User with ID {user_id} has been deleted successfully."},
                status=status.HTTP_200_OK,
            )

        except CustomUser.DoesNotExist:
            return Response(
                {"error": "User not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        except Exception as e:
            return Response(
                {"error": f"An unexpected error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
