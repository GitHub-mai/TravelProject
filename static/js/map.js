var map;

function initMap() {
    destinations = {{ destinations|safe }};
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 35.6895, lng: 139.6917}, // 初期の位置情報（東京の緯度経度）
        zoom: 3
    });
}

        // 取得した位置情報からマーカーを設定
        for (var i = 0; i < destinations.length; i++) {
            var marker = new google.maps.Marker({
                position: {lat: destinations[i].latitude, lng: destinations[i].longitude},
                map: map
            });
        }
        