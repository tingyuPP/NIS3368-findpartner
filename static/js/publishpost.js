document.addEventListener('DOMContentLoaded', () => {
  const fileInput = document.getElementById('file-input');
  const titleInput = document.getElementById('title-input');
  const contentInput = document.getElementById('content-input');
  const tagInput = document.getElementById('tag-input');
  const addTagBtn = document.getElementById('add-tag-btn');
  const tagsContainer = document.getElementById('tag-list');
  const categorySelect = document.getElementById('category-select');
  const publishBtn = document.getElementById('publish-btn');
  const cancelBtn = document.getElementById('cancel-btn');

  const tags = [];
  const hotTags = ['标签1', '标签2', '标签3'];

  addTagBtn.addEventListener('click', () => {
    const tag = tagInput.value.trim();
    if (tag) {
      tags.push(tag);
      renderTags();
      tagInput.value = '';
    }
  });

  hotTags.forEach(tag => {
    const tagElement = document.createElement('span');
    tagElement.textContent = tag;
    tagElement.classList.add('hot-tag-item');
    tagElement.addEventListener('click', () => {
      tags.push(tag);
      renderTags();
    });
    tagsContainer.appendChild(tagElement);
  });

  publishBtn.addEventListener('click', () => {
    const title = titleInput.value.trim();
    const content = contentInput.value.trim();
    const category = categorySelect.value;
    const files = fileInput.files;

    if (title && content && category) {
      const formData = new FormData();
      formData.append('title', title);
      formData.append('content', content);
      formData.append('category', category);
      tags.forEach(tag => formData.append('tags', tag));
      for (let i = 0; i < files.length; i++) {
        formData.append('files', files[i]);
      }

      fetch('/your-backend-endpoint/', {
        method: 'POST',
        body: formData,
        headers: {
          'X-CSRFToken': getCookie('csrftoken') // 如果使用 Django，需要添加 CSRF token
        }
      })
      .then(response => response.json())
      .then(data => {
        if (data.success) {
          alert('发布成功');
          resetForm();
        } else {
          alert('发布失败: ' + data.error);
        }
      })
      .catch(error => {
        console.error('Error:', error);
        alert('发布失败');
      });
    } else {
      alert('请填写完整信息');
    }
  });

  cancelBtn.addEventListener('click', resetForm);

  function renderTags() {
    tagsContainer.innerHTML = '';
    tags.forEach(tag => {
      const tagElement = document.createElement('span');
      tagElement.textContent = tag;
      tagElement.classList.add('tag-item');
      tagsContainer.appendChild(tagElement);
    });
  }

  function resetForm() {
    titleInput.value = '';
    contentInput.value = '';
    tagInput.value = '';
    tags.length = 0;
    renderTags();
  }

  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
});