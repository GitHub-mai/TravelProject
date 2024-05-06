/*
let map;

async function initMap() {
    const { Map } = await google.maps.importLibrary("maps");
    const { AdvancedMarkerView } = await google.maps.importLibrary("marker");
    map = new Map(document.getElementById("map"), {
        zoom: 4,
        center: { lat: 42, lng: 141 },
        mapId: "DEMO_MAP_ID",
    });

    const marker = new AdvancedMarkerView({
        map: map,
        position: { lat: 42, lng: 141 },
        title: "Test",
    });
}


// window.initMap = initMap;
initMap();
*/


/*
function initMap() {
    const map = new google.maps.Map(document.getElementById('map'), {
        zoom: 4,
        center: {lat: 42, lng: 141}
    });
    google.maps.event.addListener(map, 'click', event => addPingonMap(event, map));
}

function addPingonMap(event, map){
    const lat = event.lating.lat();
    const lng = event.lating.lng();
    const marker = new google.maps.Marker({
        postion: {let, lng},
        map
    });
}

window.initMap = initMap;
*/

var map;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 35.6895, lng: 139.6917}, // 初期の位置情報（東京の緯度経度）
        zoom: 8
    });

    // マップ上でクリックが発生したときのイベントリスナーを追加
    map.addListener('click', function(event) {
        placeMarker(event.latLng); // クリックした位置情報を渡してマーカーを追加
    });
}

// マーカーを追加する関数
function placeMarker(location) {
    var marker = new google.maps.Marker({
        position: location,
        map: map
    });

    // マーカーの位置情報をフォームに設定
    document.getElementById('id_latitude').value = location.lat();
    document.getElementById('id_longitude').value = location.lng();
}
