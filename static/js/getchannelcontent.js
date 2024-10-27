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
    var dynamicContent = document.getElementById('dynamic-content');
    dynamicContent.innerHTML = '';

    let url = '';
    if (channel === 'recommend') {
        url = '/dashboard/recommend';
    } else if (channel === 'sports') {
        url = '/dashboard/sports';
    } else if (channel === 'study') {
        url = '/dashboard/study';
    } else if (channel === 'food') {
        url = '/dashboard/food';
    } else if (channel === 'games') {
        url = '/dashboard/games';
    } else if (channel === 'travel') {
        url = '/dashboard/travel';
    } else if (channel === 'emotion') {
        url = '/dashboard/emotion';
    }

    // 使用 fetch API 加载 HTML 内容
    if (url) {
        fetch(url)
            .then(response => response.text())
            .then(data => {
                dynamicContent.innerHTML = data;
                executeScripts(dynamicContent);
            })
            .catch(error => console.error('Error loading content:', error));
    }
}

function executeScripts(element) {
    const scripts = element.querySelectorAll('script');
    scripts.forEach(script => {
        if (script.src) {
            const newScript = document.createElement('script');
            newScript.src = script.src;
            newScript.onload = () => {
                console.log(`Script loaded: ${script.src}`);
                if (script.src.includes('/static/js/waterfallgetcards/recommend.js')) {
                    initializeWaterfall_recommend();
                }
                else if (script.src.includes('/static/js/waterfallgetcards/sports.js')) {
                    initializeWaterfall_sports();
                }
                else if (script.src.includes('/static/js/waterfallgetcards/study.js')) {
                    initializeWaterfall_study();
                }
                else if (script.src.includes('/static/js/waterfallgetcards/food.js')) {
                    initializeWaterfall_food();
                }
                else if (script.src.includes('/static/js/waterfallgetcards/games.js')) {
                    initializeWaterfall_games();
                }
                else if (script.src.includes('/static/js/waterfallgetcards/travel.js')) {
                    initializeWaterfall_travel();
                }
                else if (script.src.includes('/static/js/waterfallgetcards/emotion.js')) {
                    initializeWaterfall_emotion();
                }
            };
            document.head.appendChild(newScript);
        } else {
            const newScript = document.createElement('script');
            newScript.textContent = script.textContent;
            document.head.appendChild(newScript).parentNode.removeChild(newScript);
            console.log('Inline script executed');
        }
    });
}

// 初始化默认频道
document.addEventListener('DOMContentLoaded', function() {
    handleChannelClick('recommend');
});