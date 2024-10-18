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
    var reg__username = $("#reg__username").val();
    var reg__email = $("#reg__email").val();
    var reg__password = $("#reg__password").val();
    var reg__password2 = $("#repeat__password").val();
    //检查以上四个字段是否为空，非空则报错
    if (reg__username == "" || reg__email == "" || reg__password == "" || reg__password2 == "") {
      alert("请填入所有字段！");
      return;
    }
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
  });
});
