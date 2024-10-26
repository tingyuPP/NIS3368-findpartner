function initializeChangeInfo() {
  // 创建ObsClient实例
  var obsClient = new ObsClient({
    access_key_id: "FTCMA0RFFEFYAHZCTUNR",
    secret_access_key: "DtOPu5ExOARQuMZHAGewDVzryaH1ht7gSWlflsJ5",
    server: "https://obs.cn-east-3.myhuaweicloud.com",
    timeout: 3000, // 设置超时时间
  });

  const fileInput = document.getElementById("file-input");
  const imageUrlInput = document.getElementById("image-url");
  const filePreview = document.getElementById("file-preview");
  const fileInputLabel = document.getElementById("file-input-label");

  filePreview.innerHTML = "";

  async function uploadToOBS(file) {
    return new Promise((resolve, reject) => {
      const fileName = `images/${Date.now()}_${file.name}`;
      obsClient.putObject(
        {
          Bucket: "findpartner",
          Key: fileName,
          SourceFile: file,
        },
        (err, result) => {
          if (err) {
            alert("上传到OBS失败");
          } else {
            const imageUrl = `https://findpartner.obs.cn-east-3.myhuaweicloud.com/${fileName}`;
            //console.log(imageUrl);
            resolve(imageUrl);
          }
        }
      );
    });
  }

  fileInput.addEventListener("change", async (event) => {
    const file = event.target.files[0];
    if (file) {
      // 限制文件大小
      const maxSize = 5 * 1024 * 1024; // 5MB
      if (file.size > maxSize) {
        alert("文件大小超过限制，请选择小于 5MB 的文件");
        return;
      }

      // 显示图片预览
      const reader = new FileReader();
      reader.onload = (e) => {
        filePreview.innerHTML = `<img src="${e.target.result}" alt="Image Preview" class="preview-img">`;
      };
      reader.readAsDataURL(file);

      // 隐藏“选择封面图”按钮
      fileInput.style.display = "none";
      fileInputLabel.style.display = "none";
      // 上传图片到华为云OBS
      const imageUrl = await uploadToOBS(file);
      imageUrlInput.value = imageUrl;
      console.log(imageUrlInput.value);
      console.log(111)
      // 将图片URL设置为预览图的src
      filePreview.querySelector("img").src = imageUrl;
    }
  });
}

