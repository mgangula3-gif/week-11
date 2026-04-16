<html>
<body>
<h2>Login</h2>

<form action="login.jsp" method="post">
    Username: <input type="text" name="username"><br><br>
    Password: <input type="password" name="password"><br><br>
    <input type="submit" value="Login">
</form>

<%@ page import="java.sql.*, com.db.DBConnection" %>

<%
String user = request.getParameter("username");
String pass = request.getParameter("password");

if(user != null && pass != null){
    Connection con = DBConnection.getConnection();

    PreparedStatement ps = con.prepareStatement(
        "SELECT * FROM users WHERE username=? AND password=?"
    );

    ps.setString(1, user);
    ps.setString(2, pass);

    ResultSet rs = ps.executeQuery();

    if(rs.next()){
        response.sendRedirect("success.jsp");
    } else {
        response.sendRedirect("error.jsp");
    }
}
%>

</body>
</html>
