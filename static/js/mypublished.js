function initializePublished() {
  // 使用 fetch 或 jQuery 的 AJAX 请求后端数据
  fetch("/get-my-published-notice/")
    .then((response) => response.json())
    .then((data) => {
      console.log(data); // 输出数据供后续处理
      // 可在此处理数据，例如渲染到页面
      printNotice(data.notice_list);
    })
    .catch((error) => console.error("Error fetching data:", error));
}

function printNotice(data) {
  const messagesContainer = document.getElementById("message-container"); // 假设你有一个容器ID为messages-container
  if (!data || data.length === 0) {
    const messageItem = document.createElement("li");
    messageItem.className = "message-item";
    messageItem.textContent = "尚未发布任何需求";
    messagesContainer.appendChild(messageItem);
    return;
  }
  data.forEach((item) => {
    const messageItem = document.createElement("li");
    messageItem.className = "message-item";

    // 注意！！！！这里下面的“头像”均为写错了，实际为帖子封面。
    const userNotice = document.createElement("a");
    userNotice.className = "user-notice";

    const noticeImg = document.createElement("img");
    noticeImg.className = "notice-item";
    noticeImg.src = item.image; // 使用item中的头像URL
    noticeImg.alt = "用户头像"; // 设置图像描述

    userNotice.appendChild(noticeImg);

    // 消息主内容部分
    const mainContent = document.createElement("div");
    mainContent.className = "main";

    const inforTiezi = document.createElement("div");
    inforTiezi.className = "infor-tiezi";

    // 帖子信息
    const tieziInfo = document.createElement("div");
    tieziInfo.className = "tiezi-info";

    const titleLink = document.createElement("a");
    titleLink.textContent = item.title; // 使用item中的标题

    const interactionHint = document.createElement("div");
    interactionHint.className = "interaction-hint";

    const dateSpan = document.createElement("span");
    dateSpan.textContent = item.time; // 使用item中的日期

    interactionHint.appendChild(dateSpan);

    tieziInfo.appendChild(titleLink);
    tieziInfo.appendChild(interactionHint);

    // 帖子内容
    const interactionContent = document.createElement("div");
    interactionContent.className = "interaction-content";

    const contentSpan = document.createElement("span");
    contentSpan.textContent = item.description; // 使用item中的内容

    interactionContent.appendChild(contentSpan);

    // 将内容组织到主内容结构中
    inforTiezi.appendChild(tieziInfo);
    inforTiezi.appendChild(interactionContent);

    mainContent.appendChild(inforTiezi);

    // 将所有部分添加到消息项
    messageItem.appendChild(userNotice);
    messageItem.appendChild(mainContent);

    // 将消息项添加到容器中
    messagesContainer.appendChild(messageItem);

    messageItem.addEventListener("click", function () {
      openNoteDetail(item.id);
    });
  });
}

function openNoteDetail(id) {
  // 更新浏览器地址栏
  history.pushState(null, null, `/main/${id}/`);
  //刷新页面
  location.reload();
}
