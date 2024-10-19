document.addEventListener('DOMContentLoaded', () => {
  const fileInput = document.getElementById('fileInput');
  const titleInput = document.getElementById('titleInput');
  const contentInput = document.getElementById('contentInput');
  const tagInput = document.getElementById('tagInput');
  const addTagBtn = document.getElementById('addTagBtn');
  const tagsContainer = document.getElementById('tagsContainer');
  const hotTagsContainer = document.getElementById('hotTagsContainer');
  const categorySelect = document.getElementById('categorySelect');
  const publishBtn = document.getElementById('publishBtn');
  const cancelBtn = document.getElementById('cancelBtn');

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
    hotTagsContainer.appendChild(tagElement);
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
});