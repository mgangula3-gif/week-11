<html>
<body>
<h2>Change Password</h2>

<form action="changePassword.jsp" method="post">
    Username: <input type="text" name="username"><br><br>
    Old Password: <input type="password" name="oldpass"><br><br>
    New Password: <input type="password" name="newpass"><br><br>
    <input type="submit" value="Change Password">
</form>

<%@ page import="java.sql.*, com.db.DBConnection" %>

<%
String user = request.getParameter("username");
String oldpass = request.getParameter("oldpass");
String newpass = request.getParameter("newpass");

if(user != null && oldpass != null && newpass != null){
    Connection con = DBConnection.getConnection();

    PreparedStatement ps = con.prepareStatement(
        "UPDATE users SET password=? WHERE username=? AND password=?"
    );

    ps.setString(1, newpass);
    ps.setString(2, user);
    ps.setString(3, oldpass);

    int i = ps.executeUpdate();

    if(i > 0){
        out.println("Password Changed Successfully!");
    } else {
        out.println("Invalid Old Password!");
    }
}
%>

</body>
</html>
