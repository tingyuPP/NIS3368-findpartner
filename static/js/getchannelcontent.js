function handleChannelClick(channel) {
        // 移除所有栏目上的 active 类
        var channels = document.querySelectorAll('.channel');
        channels.forEach(function(ch) {
            ch.classList.remove('active');
        });

        // 为点击的栏目添加 active 类
        var activeChannel = document.getElementById('channel-' + channel);
        activeChannel.classList.add('active');

        // 调用相应的 JS 函数来显示后端给的信息
        fetchChannelData(channel);
    }

    function fetchChannelData(channel) {
        // 这里可以添加你的 AJAX 请求或其他逻辑来获取后端数据
        console.log('Fetching data for channel:', channel);
        // 示例：假设你有一个函数 showChannelData 来显示数据
        showChannelData(channel);
    }

    function showChannelData(channel) {
        // 示例函数：根据频道显示数据
        console.log('Showing data for channel:', channel);
        // 这里可以添加你的逻辑来更新页面内容
    }
