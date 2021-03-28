'use strict';

class Point2D{

    constructor(x, y){
        this.x = x;
        this.y = y;
    }

    /**
     * 
     * @param {Point2D} p2D 
     */
    move(p2D){
        this.x += p2D.x;
        this.y += p2D.y;
    }
}

function getData(){
    let point1X = document.getElementById('point1x');
    let point2X = document.getElementById('point2x');
    let point3X = document.getElementById('point3x');

    let point1Y = document.getElementById('point1y');
    let point2Y = document.getElementById('point2y');
    let point3Y = document.getElementById('point3y');

    let arr = [];
    arr.push(new Point2D(parseInt(point1X.value), parseInt(point1Y.value)));
    arr.push(new Point2D(parseInt(point2X.value), parseInt(point2Y.value)));
    arr.push(new Point2D(parseInt(point3X.value), parseInt(point3Y.value)));

    return arr;
}

/**
 * 
 * @param {*} ctx 
 * @param {Point2D} p1 
 * @param {Point2D} p2 
 * @param {Point2D} p3 
 * @param {*} color 
 */
function drawTriangle(ctx, p1, p2, p3, color = 'rgb(0, 250, 250)'){
    ctx.strokeStyle = color;
    ctx.beginPath();

    ctx.moveTo(p1.x, p1.y);
    ctx.lineTo(p2.x, p2.y);
    ctx.lineTo(p3.x, p3.y);
    ctx.lineTo(p1.x, p1.y);
    ctx.stroke();
}

/**
 * 
 * @param {*} ctx 
 * @param {Point2D} p1 
 * @param {Point2D} p2 
 * @param {Point2D} p3 
 */
function paintOver(ctx, p1, p2, p3, color = 'rgb(0, 250, 250)'){

    // k = (p3.y - p1.y) / (p3.x - p1.x)
    let k1 = (p2.x - p1.x) / (p2.y - p1.y);
    let k2 = (p3.x - p1.x) / (p3.y - p1.y);

    ctx.strokeStyle = color;
    ctx.beginPath();

    let x1 = 0;
    let x2 = 0;
    for (let y = p1.y; y < p2.y; y++){
        x1 = p1.x + (y - p1.y) * k1;
        x2 = p1.x + (y - p1.y) * k2;
        ctx.moveTo(x1, y);
        ctx.lineTo(x2, y);
    }
    ctx.stroke();

    let k3 = (p2.x - p3.x) / (p2.y - p3.y);
    let x = x2;
    ctx.beginPath();
    for (let y = p2.y; y < p3.y; y++){
        x1 = x + (y - p2.y) * k2;
        x2 = p2.x + (y - p2.y) * k3;
        ctx.moveTo(x1, y);
        ctx.lineTo(x2, y);
    }
    ctx.stroke();
}

const canvas = document.querySelector('.canvas');
const ctx = canvas.getContext('2d');

const btnStart = document.querySelector('.btn');
btnStart.addEventListener('click', () => {
    let arr = getData();

    ctx.fillStyle = 'rgb(102, 109, 104)';
    ctx.fillRect(0, 0, canvas.width, canvas.height); // clear canvas

    drawTriangle(ctx, ...arr);
    
});

const btnPaint = document.querySelector('.btn-paint');
btnPaint.addEventListener('click', () => {
    let arr = getData();
    paintOver(ctx, ...arr, 'black');
});
