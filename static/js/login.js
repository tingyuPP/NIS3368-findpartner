$(document).ready(function () {
  $("#signup").click(function () {
    $(".pinkbox").css("transform", "translateX(80%)");
    $(".signin").addClass("nodisplay");
    $(".signup").removeClass("nodisplay");
  });

  $("#signin").click(function () {
    $(".pinkbox").css("transform", "translateX(0%)");
    $(".signup").addClass("nodisplay");
    $(".signin").removeClass("nodisplay");
  });

  $("#register").click(function (event) {

    event.preventDefault();

    var reg__username = $("#reg__username").val();
    //var reg__email = $("#reg__email").val();
    var reg__password = $("#reg__password").val();
    var reg__password2 = $("#repeat__password").val();
    //检查以上四个字段是否为空，非空则报错
    if (
      reg__username == "" ||
      //reg__email == "" ||
      reg__password == "" ||
      reg__password2 == ""
    ) {
      alert("请填入所有字段！");
      return;
    }
    //检查用户名合法性
    if(!validateUsername()){
      return;
    }
    //检查邮箱合法性
    //if(!validateEmail()){
    //  return;
    //}
    //检查密码合法性
    if(!validatePassword()){
      return;
    }
    //检查两次密码是否一致
    if(!checkPassword()){
      return;
    }
    $("#register-form").submit();
  });

  $("#login").click(function (event) {
    event.preventDefault();

    var log__username = $("#log__username").val();
    var log__password = $("#log__password").val();
    //检查以上两个字段是否为空，非空则报错
    if (log__username == "" || log__password == "") {
      alert("请填入所有字段！");
      return;
    }

    $("#login-form").submit();
  });

  $("#reg__username").change(function (event) {
    validateUsername();
  });

  //$("#reg__email").change(function (event) {
  //  validateEmail();
  //});

  $("#reg__password").change(function (event) {
    validatePassword();
  });

  $("#repeat__password").change(function (event) {
    checkPassword();
  });

  function validateUsername() {
    var reg__username = $("#reg__username").val();
    var reg = /^[a-zA-Z0-9]{6,18}$/;
    if (!reg.test(reg__username)) {
      alert("用户名不合法，请输入6-18位字母或数字！");
      return false;
    }
    return true;
  }

  function validateEmail() {
    var reg__email = $("#reg__email").val();
    var reg = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!reg.test(reg__email)) {
      alert("邮箱不合法，请输入正确的邮箱格式！");
      return false;
    }
    return true;
  }

  function validatePassword() {
    var reg__password = $("#reg__password").val();
    var reg = /^[a-zA-Z0-9]{8,18}$/;
    if (!reg.test(reg__password)) {
      alert("密码不合法，请输入8-18位字母或数字！");
      return false;
    }
    return true;
  }

  function checkPassword() {
    var reg__password = $("#reg__password").val();
    var reg__password2 = $("#repeat__password").val();
    if (reg__password != reg__password2) {
      alert("两次输入密码不一致！");
      return false;
    }
    return true;
  }
});
