
// 创建ObsClient实例
var obsClient = new ObsClient({
  access_key_id: 'FTCMA0RFFEFYAHZCTUNR',
  secret_access_key: 'DtOPu5ExOARQuMZHAGewDVzryaH1ht7gSWlflsJ5',
  server: 'https://obs.cn-east-3.myhuaweicloud.com',
  timeout: 3000, // 设置超时时间
});

document.addEventListener('DOMContentLoaded', () => {
  const fileInput = document.getElementById('file-input');
  const filePreview = document.getElementById('file-preview');
  const uploadProgress = document.getElementById('upload-progress');
  const titleInput = document.getElementById('title-input');
  const contentInput = document.getElementById('content-input');
  const addTagBtn = document.getElementById('add-tag-btn');
  const tagsContainer = document.getElementById('tag-list');
  const categorySelect = document.getElementById('category-select');
  const publishBtn = document.getElementById('publish-btn');
  const cancelBtn = document.getElementById('cancel-btn');
  const fileInputLabel = document.querySelector('label[for="file-input"]');

  const tags = [];

  addTagBtn.addEventListener('click', () => {
    const newTagInput = document.createElement('input');
    newTagInput.type = 'text';
    newTagInput.classList.add('tag-input');
    newTagInput.placeholder = '输入标签';
    newTagInput.addEventListener('keypress', (event) => {
      if (event.key === 'Enter') {
        const tag = newTagInput.value.trim();
        if (tag) {
          tags.push(tag);
          renderTags();
        }
      }
    });
    tagsContainer.appendChild(newTagInput);
    newTagInput.focus();
    addTagBtn.style.display = 'none';
  });

  publishBtn.addEventListener('click', async () => {
    const title = titleInput.value.trim();
    const content = contentInput.value.trim();
    const category = categorySelect.value;

    if (!title || !content || !category) {
      alert('请填写完整信息');
      return;
    }

    const imageUrl = filePreview.querySelector('img')?.src;
    if (!imageUrl) {
      alert('请上传封面图');
      return;
    }

    await sendToServer(imageUrl);
  });

  cancelBtn.addEventListener('click', () => {
    window.location.href = '/dashboard/';
  });

  function renderTags() {
    tagsContainer.innerHTML = '';
    tags.forEach(tag => {
      const tagElement = document.createElement('span');
      tagElement.textContent = tag;
      tagElement.classList.add('tag-item');
      tagsContainer.appendChild(tagElement);
    });
    tagsContainer.appendChild(addTagBtn);
    addTagBtn.style.display = 'inline-block';
  }

  function resetForm() {
    titleInput.value = '';
    contentInput.value = '';
    tags.length = 0;
    renderTags();
    filePreview.innerHTML = '';
    fileInput.value = '';
    fileInput.style.display = 'block';
    fileInputLabel.style.display = 'block';
    uploadProgress.style.display = 'none';
    uploadProgress.value = 0;
  }

  fileInput.addEventListener('change', async (event) => {
    const file = event.target.files[0];
    if (file) {
      // 限制文件大小
      const maxSize = 5 * 1024 * 1024; // 5MB
      if (file.size > maxSize) {
        alert('文件大小超过限制，请选择小于 5MB 的文件');
        return;
      }

      // 显示图片预览
      const reader = new FileReader();
      reader.onload = (e) => {
        filePreview.innerHTML = `<img src="${e.target.result}" alt="Image Preview" class="preview-img">`;
      };
      reader.readAsDataURL(file);

      // 隐藏“选择封面图”按钮
      fileInput.style.display = 'none';
      fileInputLabel.style.display = 'none';

      // 上传图片到华为云OBS
      const imageUrl = await uploadToOBS(file);


      // 将图片URL设置为预览图的src
      filePreview.querySelector('img').src = imageUrl;
    }
  });

  async function uploadToOBS(file) {
    return new Promise((resolve, reject) => {
      const fileName = `images/${Date.now()}_${file.name}`;
      obsClient.putObject({
        Bucket: 'findpartner',
        Key: fileName,
        SourceFile: file
      }, (err, result) => {
        if (err) {
          alert('上传到OBS失败');
          
        } else {
          const imageUrl = `https://findpartner.obs.cn-east-3.myhuaweicloud.com/${fileName}`;
          console.log(imageUrl);
        }
      });
    });
  }

  function sendToServer(imageUrl) {
    return new Promise((resolve, reject) => {
      const title = titleInput.value.trim();
      const content = contentInput.value.trim();
      const category = categorySelect.value;
      const tags = getTags();

      if (!title || !content || !category) {
        alert('请填写完整信息');
        return;
      }

      const postData = {
        title,
        content,
        category,
        tags,
        imageUrl
      };

      const xhr = new XMLHttpRequest();
      xhr.open('POST', '/savePost', true);
      xhr.setRequestHeader('Content-Type', 'application/json');

      xhr.onload = () => {
        if (xhr.status === 200) {
          alert('发布成功');
          resetForm();
          resolve();
        } else {
          alert('发布失败');
          reject();
        }
      };

      xhr.onerror = () => {
        alert('发布失败');
        reject();
      };

      xhr.send(JSON.stringify(postData));
    });
  }

  function getTags() {
    return tags.map(tag => tag.trim()).filter(tag => tag);
  }
});