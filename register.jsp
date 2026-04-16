<html>
<body>
<h2>Register</h2>

<form action="register.jsp" method="post">
    Username: <input type="text" name="username"><br><br>
    Password: <input type="password" name="password"><br><br>
    <input type="submit" value="Register">
</form>

<%@ page import="java.sql.*, com.db.DBConnection" %>

<%
String user = request.getParameter("username");
String pass = request.getParameter("password");

if(user != null && pass != null){
    Connection con = DBConnection.getConnection();

    PreparedStatement ps = con.prepareStatement(
        "INSERT INTO users(username,password) VALUES(?,?)"
    );

    ps.setString(1, user);
    ps.setString(2, pass);

    int i = ps.executeUpdate();

    if(i > 0){
        out.println("Registration Successful!");
    } else {
        out.println("Error!");
    }
}
%>

</body>
</html>
