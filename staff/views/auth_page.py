from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_page(request):
    # Xử lý khi người dùng ấn nút Đăng nhập
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Hàm authenticate sẽ lấy raw password băm ra và so với DB
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user) # Tạo session lưu trạng thái đăng nhập
            return redirect("/dashboard/")

        # Báo lỗi nếu sai tài khoản/mật khẩu
        return render(request, "login.html", {
            "error": "Tên đăng nhập hoặc mật khẩu không chính xác!"
        })

    # Mặc định sẽ render form cho GET request và các request khác
    return render(request, "login.html")