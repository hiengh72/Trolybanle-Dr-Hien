import streamlit as st

# Tiêu đề của ứng dụng
st.title("Trợ Lý Tiêu Dùng Tiết Kiệm")

# Hướng dẫn khách hàng
st.header("Chào bạn! Bạn cần giúp đỡ vấn đề gì hay tìm sản phẩm nào không?")

# Tạo một ô nhập liệu để khách hàng có thể nhập nhu cầu
user_input = st.text_input("Hãy nhập nhu cầu hoặc sản phẩm bạn muốn tìm kiếm:")

# Hiện thị phản hồi
if user_input:
    st.write(f"Bạn đã nhập nhu cầu, sản phẩm: {user_input}. Chúng tôi sẽ hỗ trợ bạn ngay lập tức!")