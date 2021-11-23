function findNewPoint(x, y, angle, distance) {
    var result = {};

    result.x = Math.round(Math.cos(angle * Math.PI / 180) * distance + x);
    result.y = Math.round(Math.sin(angle * Math.PI / 180) * distance + y);

    return result;
}

var newPoint = findNewPoint(10, 20, 10, 200);
console.log('newPoint:', newPoint);