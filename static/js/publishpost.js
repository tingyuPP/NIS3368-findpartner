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

  publishBtn.addEventListener('click', () => {
    const title = titleInput.value.trim();
    const content = contentInput.value.trim();
    const category = categorySelect.value;
    if (title && content && category) {
      alert('发布成功');
      resetForm();
    } else {
      alert('请填写完整信息');
    }
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
    document.querySelector('label[for="file-input"]').style.display = 'block';
    uploadProgress.style.display = 'none';
    uploadProgress.value = 0;
  }

  fileInput.addEventListener('change', async (event) => {
    const file = event.target.files[0];
    if (file) {
      // 限制文件大小
      const maxSize = 2 * 1024 * 1024; // 2MB
      if (file.size > maxSize) {
        alert('文件大小超过限制，请选择小于 2MB 的文件');
        return;
      }

      // 压缩图片
      const compressedFile = await compressImage(file);

      // 转换为 Base64
      const base64String = await convertToBase64(compressedFile);
      console.log(base64String);

      // 发送至后端并更新进度条
      await sendToServer(base64String);
    }
  });

  function compressImage(file) {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onload = (event) => {
        const img = new Image();
        img.src = event.target.result;
        img.onload = () => {
          const canvas = document.createElement('canvas');
          const ctx = canvas.getContext('2d');
          const maxWidth = 800;
          const maxHeight = 800;
          let width = img.width;
          let height = img.height;

          if (width > height) {
            if (width > maxWidth) {
              height *= maxWidth / width;
              width = maxWidth;
            }
          } else {
            if (height > maxHeight) {
              width *= maxHeight / height;
              height = maxHeight;
            }
          }

          canvas.width = width;
          canvas.height = height;
          ctx.drawImage(img, 0, 0, width, height);
          canvas.toBlob((blob) => {
            resolve(blob);
          }, 'image/jpeg', 0.9);
        };
      };
      reader.onerror = (error) => reject(error);
    });
  }

  function convertToBase64(file) {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onload = () => resolve(reader.result);
      reader.onerror = (error) => reject(error);
    });
  }

  function sendToServer(base64String) {
    return new Promise((resolve, reject) => {
      const xhr = new XMLHttpRequest();
      xhr.open('POST', '/upload', true);
      xhr.setRequestHeader('Content-Type', 'application/json');

      xhr.upload.onprogress = (event) => {
        if (event.lengthComputable) {
          const percentLoaded = Math.round((event.loaded / event.total) * 100);
          uploadProgress.value = percentLoaded;
          uploadProgress.style.display = 'block';
        }
      };

      xhr.onloadstart = () => {
        uploadProgress.style.display = 'block';
      };

      xhr.onloadend = () => {
        uploadProgress.style.display = 'none';
        if (xhr.status === 200) {
          alert('上传成功');
          resolve();
        } else {
          alert('上传失败');
          reject();
        }
      };

      xhr.onerror = () => {
        uploadProgress.style.display = 'none';
        alert('上传失败');
        reject();
      };

      xhr.send(JSON.stringify({ image: base64String }));
    });
  }
});