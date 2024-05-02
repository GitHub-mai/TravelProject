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
