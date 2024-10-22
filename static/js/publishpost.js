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

  fileInput.addEventListener('change', (event) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onloadstart = () => {
        uploadProgress.style.display = 'block';
      };
      reader.onprogress = (e) => {
        if (e.lengthComputable) {
          const percentLoaded = Math.round((e.loaded / e.total) * 100);
          uploadProgress.value = percentLoaded;
        }
      };
      reader.onload = (e) => {
        const img = document.createElement('img');
        img.src = e.target.result;
        img.classList.add('preview-img');
        filePreview.innerHTML = '';
        filePreview.appendChild(img);
        fileInput.style.display = 'none';
        document.querySelector('label[for="file-input"]').style.display = 'none';
        uploadProgress.style.display = 'none';
      };
      reader.readAsDataURL(file);
    }
  });
});