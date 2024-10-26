function initializeWaterfall_study() {
  console.log("waterfallgetcards.js loaded");
  
  const list = [
    { src: "https://tse1-mm.cn.bing.net/th/id/OIP-C.Zte3ljd4g6kqrWWyg-8fhAHaEo?w=264&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7" },
    { src: "https://tse1-mm.cn.bing.net/th/id/OIP-C.cGc4c8dVlqnfV3uwcS1IogHaE8?w=260&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7" },
    { src: "https://tse1-mm.cn.bing.net/th/id/OIP-C.Zte3ljd4g6kqrWWyg-8fhAHaEo?w=264&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7" },
    { src: "https://tse4-mm.cn.bing.net/th/id/OIP-C.N0USLldg_iKDGVKT12vB4AHaEK?w=292&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7" },
    { src: "https://tse1-mm.cn.bing.net/th/id/OIP-C.jzcWzXf_uts2sgE2WChuCQHaEo?w=263&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7" },
    { src: "https://tse1-mm.cn.bing.net/th/id/OIP-C.Zte3ljd4g6kqrWWyg-8fhAHaEo?w=264&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7" },
    { src: "https://fuss10.elemecdn.com/a/3f/3302e58f9a181d2509f3dc0fa68b0jpeg.jpeg" },
    { src: "https://fuss10.elemecdn.com/1/34/19aa98b1fcb2781c4fba33d850549jpeg.jpeg" },
    { src: "https://fuss10.elemecdn.com/d/e6/c4d93a3805b3ce3f323f7974e6f78jpeg.jpeg" },
    { src: "https://fuss10.elemecdn.com/0/6f/e35ff375812e6b0020b6b4e8f9583jpeg.jpeg" },
    { src: "https://fuss10.elemecdn.com/9/bb/e27858e973f5d7d3904835f46abbdjpeg.jpeg" },
    { src: "https://fuss10.elemecdn.com/3/28/bbf893f792f03a54408b3b7a7ebf0jpeg.jpeg" },
    { src: "https://fuss10.elemecdn.com/2/11/6535bcfb26e4c79b48ddde44f4b6fjpeg.jpeg" },
    { src: "https://tse4-mm.cn.bing.net/th/id/OIP-C.N0USLldg_iKDGVKT12vB4AHaEK?w=292&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7" },
    { src: "https://tse1-mm.cn.bing.net/th/id/OIP-C.jzcWzXf_uts2sgE2WChuCQHaEo?w=263&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7" },
    { src: "https://tse3-mm.cn.bing.net/th/id/OIP-C.YzEeJqgWky6RQMatrMd6-gHaHa?w=170&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7" },
    { src: "https://tse3-mm.cn.bing.net/th/id/OIP-C.YzEeJqgWky6RQMatrMd6-gHaHa?w=170&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7" },
    { src: "https://tse1-mm.cn.bing.net/th/id/OIP-C.Zte3ljd4g6kqrWWyg-8fhAHaEo?w=264&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7" },
    { src: "https://tse4-mm.cn.bing.net/th/id/OIP-C.N0USLldg_iKDGVKT12vB4AHaEK?w=292&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7" },
    { src: "https://tse1-mm.cn.bing.net/th/id/OIP-C.jzcWzXf_uts2sgE2WChuCQHaEo?w=263&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7" },
    { src: "https://tse1-mm.cn.bing.net/th/id/OIP-C.Zte3ljd4g6kqrWWyg-8fhAHaEo?w=264&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7" },
    { src: "https://tse1-mm.cn.bing.net/th/id/OIP-C.cGc4c8dVlqnfV3uwcS1IogHaE8?w=260&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7" },
    { src: "https://cdn.jsdelivr.net/gh/zlh123123/MyPictures/090d27fd04c81ca2bf644c4b3f6e2134487203952.jpg@1256w_708h_!web-article-pic.png" },
    { src: "https://findpartner.obs.cn-east-3.myhuaweicloud.com/images/1729752099760_0b85baf6d4351104402a02f669ea7b961125377114.png%401256w_704h_%21web-article-pic.png" },
    { src: "https://findpartner.obs.cn-east-3.myhuaweicloud.com/images/1729752099760_0b85baf6d4351104402a02f669ea7b961125377114.png%401256w_704h_%21web-article-pic.png" },
    { src: "https://findpartner.obs.cn-east-3.myhuaweicloud.com/images/1729752099760_0b85baf6d4351104402a02f669ea7b961125377114.png%401256w_704h_%21web-article-pic.png" },
  ];

  const feedsContainer = document.getElementById('feeds-container');

  list.forEach(item => {
    const card = document.createElement('div');
    card.className = 'card';

    card.dataset.id = item.id; // 设置帖子ID

    const img = document.createElement('img');
    img.setAttribute('data-src', item.src);
    img.className = 'lazy';

    const footer = document.createElement('div');
    footer.className = 'footer';

    const title = document.createElement('a');
    title.className = 'title';
    title.innerHTML = '<span>这是具体内容</span>';

    const authorWrapper = document.createElement('div');
    authorWrapper.className = 'author-wrapper';

    const author = document.createElement('a');
    author.className = 'author';

    const authorAvatar = document.createElement('img');
    authorAvatar.className = 'author-avatar';
    authorAvatar.src = item.src;

    const name = document.createElement('span');
    name.className = 'name';
    name.textContent = '这是名字';

    author.appendChild(authorAvatar);
    author.appendChild(name);

    const likeWrapper = document.createElement('span');
    likeWrapper.className = 'like-wrapper like-active';

    



    authorWrapper.appendChild(author);
    authorWrapper.appendChild(likeWrapper);

    footer.appendChild(title);
    footer.appendChild(authorWrapper);

    card.appendChild(img);
    card.appendChild(footer);

    card.addEventListener('click', function () {
      openNoteDetail(item.id);
    });

    feedsContainer.appendChild(card);
  });

  // 懒加载功能
  const lazyImages = document.querySelectorAll('.lazy');
  const lazyLoad = () => {
    lazyImages.forEach(img => {
      if (img.getBoundingClientRect().top < window.innerHeight && img.getBoundingClientRect().bottom > 0 && getComputedStyle(img).display !== 'none') {
        img.src = img.getAttribute('data-src');
        img.classList.remove('lazy');
      }
    });

    if (lazyImages.length === 0) {
      document.removeEventListener('scroll', lazyLoad);
      window.removeEventListener('resize', lazyLoad);
      window.removeEventListener('orientationchange', lazyLoad);
   
    }
  };



  document.addEventListener('scroll', lazyLoad);
  window.addEventListener('resize', lazyLoad);
  window.addEventListener('orientationchange', lazyLoad);
  lazyLoad();
}

function openNoteDetail(id) {
  // 更新浏览器地址栏
  history.pushState(null, null, `/main/`);

  //刷新页面
  location.reload();


}