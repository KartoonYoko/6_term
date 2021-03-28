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

/**
 * 
 * @param {*} ctx 
 * @param {Point2D} p 
 */
function setPixel(ctx, p, color = 'rgb(0, 250, 250)'){

    ctx.fillStyle = color;
    ctx.fillRect( p.x, p.y, 1, 1 );
}

/**
 * Проверяет равен ли цвет пикселя color
 * @param {*} ctx 
 * @param {*} p 
 * @param {*} color 
 */
function checkPixelColor(ctx, p, color){
    let imageData = ctx.getImageData(p.x, p.y, 1, 1).data;
    let pixelColor = 'rgb(' + imageData[0] + ', ' + imageData[1] + ', ' + imageData[2] + ', ' + imageData[3] + ')';

    if (color == pixelColor){
        return true;
    }
    else{
        return false;
    }
}

/**
 * 
 * @param {*} ctx 
 * @param {Point2D} p 
 * @param {} paintColor
 */
function zatravka(ctx, p, paintColor){
    let stack = [];
    
    let pixel;
    let point = null;
    let last = null;
    stack.push(p);
    while(stack.length != 0){
        if(last){ // если рядом с последним пикселем был незакрашенный
            pixel = last;
        }
        else{
            pixel = stack.pop();
        }

        if (!checkPixelColor(ctx, pixel, paintColor)){
            setPixel(ctx, pixel, paintColor);

            last = null;
            point = new Point2D(pixel.x - 1, pixel.y);
            if (!checkPixelColor(ctx, point, paintColor)){
                stack.push(point);
                last = point;
            }
            point = new Point2D(pixel.x + 1, pixel.y);
            if (!checkPixelColor(ctx, point, paintColor)){
                stack.push(point);
                last = point;
            }
            point = new Point2D(pixel.x, pixel.y - 1);
            if (!checkPixelColor(ctx, point, paintColor)){
                stack.push(point);
                last = point;
            }
            point = new Point2D(pixel.x, pixel.y + 1);
            if (!checkPixelColor(ctx, point, paintColor)){
                stack.push(point);
                last = point;
            }
        }

    }
}

const CANVAS_COLOR = 'rgb(102, 109, 104)';

const canvas = document.querySelector('.canvas');
const ctx = canvas.getContext('2d');

const btnStart = document.querySelector('.btn');
btnStart.addEventListener('click', () => {
    let arr = getData();

    ctx.fillStyle = CANVAS_COLOR;
    ctx.fillRect(0, 0, canvas.width, canvas.height); // clear canvas

    drawTriangle(ctx, ...arr);
    
});

const btnPaint = document.querySelector('.btn-paint');
btnPaint.addEventListener('click', () => {
    let arr = getData();
    paintOver(ctx, ...arr);

    zatravka(ctx, new Point2D(300, 10), CANVAS_COLOR);
});


