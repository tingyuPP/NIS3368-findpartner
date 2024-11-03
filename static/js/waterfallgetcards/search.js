function printNotice(data) {
    const feedsContainer = document.getElementById("feeds-container");

    data.forEach((item) => {
        const card = document.createElement("div");
        card.className = "card";

        card.dataset.id = item.id; // 设置帖子ID

        const img = document.createElement("img");
        img.setAttribute("data-src", item.image);
        img.className = "lazy";

        const footer = document.createElement("div");
        footer.className = "footer";

        const title = document.createElement("a");
        title.className = "title";
        title.innerHTML = item.title;

        const authorWrapper = document.createElement("div");
        authorWrapper.className = "author-wrapper";

        const author = document.createElement("a");
        author.className = "author";
        author.href = `/my/${item.owner_id}/`;

        const authorAvatar = document.createElement("img");
        authorAvatar.className = "author-avatar";
        authorAvatar.src = item.owner_avatar;
        

        const name = document.createElement("span");
        name.className = "name";
        name.textContent = item.owner_nickname;

        author.appendChild(authorAvatar);
        author.appendChild(name);

        const likeWrapper = document.createElement("span");
        likeWrapper.className = "like-wrapper like-active";

        authorWrapper.appendChild(author);
        authorWrapper.appendChild(likeWrapper);

        footer.appendChild(title);
        footer.appendChild(authorWrapper);

        card.appendChild(img);
        card.appendChild(footer);

        img.addEventListener("click", function () {
            openNoteDetail(item.id);
        });

        feedsContainer.appendChild(card);
    });

    // 懒加载功能
    const lazyImages = document.querySelectorAll(".lazy");
    const lazyLoad = () => {
        lazyImages.forEach((img) => {
            const rect = img.getBoundingClientRect();

            if (
                rect.top < window.innerHeight &&
                rect.bottom > 0 &&
                getComputedStyle(img).display !== "none"
            ) {
                img.src = img.getAttribute("data-src");

                img.classList.remove("lazy");
            }
        });

        if (lazyImages.length === 0) {
            document.removeEventListener("scroll", lazyLoad);
            window.removeEventListener("resize", lazyLoad);
            window.removeEventListener("orientationchange", lazyLoad);
        }
    };

    document.addEventListener("scroll", lazyLoad);
    window.addEventListener("resize", lazyLoad);
    window.addEventListener("orientationchange", lazyLoad);
    lazyLoad();
}

function openNoteDetail(id) {
    // 更新浏览器地址栏
    history.pushState(null, null, `/main/${id}/`);

    //刷新页面
    location.reload();
}
