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


/**
 * Закрасить пиксель
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
 * 
 * @param {*} ctx 
 * @param {Point2D} p 
 * @param {Array} color 
 */
function checkPixelColor(ctx, p, color){
    let imageData = ctx.getImageData(p.x, p.y, 1, 1).data;
    let pixelColor = 'rgb(' + imageData[0] + ', ' + imageData[1] + ', ' + imageData[2] + ')';
    
    if (Array.isArray(color)){
        let res = false;
        color.forEach(element => {
            if (element == pixelColor) { 
                res = true;  
            }
        });
        return res;
    }
    else{

        if (color == pixelColor){
            return true;
        }
        else{
            return false;
        }
    }
}

/**
 * Получить цвет пикселя
 * 
 * @param {*} ctx 
 * @param {Point2D} p 
 * @returns {string} color
 */
function getColorOfPixel(ctx, p){
    let imageData = ctx.getImageData(p.x, p.y, 1, 1).data;
    let pixelColor = 'rgb(' + imageData[0] + ', ' + imageData[1] + ', ' + imageData[2] + ', ' + imageData[3] + ')';
    return pixelColor;
}

class Stack{

    constructor(){
        this.stack = new Set();
    }

    /**
     * 
     * @param {Point2D} p 
     */
    push(p){
        let s = 'x:' + p.x + 'y:' + p.y;
        this.stack.add(s);
    }

    /**
     * 
     * @returns {Point2D} первая точка из стека
     */
    pop_first(){
        let point = '';
        for (let item of this.stack) {
            point = item;
            break;
        }
        this.stack.delete(point);

        let x = point.indexOf('x:') + 2;
        let y = point.indexOf('y:');
        let end = point.length;
        let first = parseInt(point.slice(x, y));
        let second = parseInt(point.slice(y + 2, end));
        return new Point2D(first, second);
    }

    /**
     * 
     * @returns {Point2D} последняя точка из стека
     */
     pop(){
        let point = '';
        for (let item of this.stack) {
            point = item;
        }
        this.stack.delete(point);

        let x = point.indexOf('x:') + 2;
        let y = point.indexOf('y:');
        let end = point.length;
        let first = parseInt(point.slice(x, y));
        let second = parseInt(point.slice(y + 2, end));
        return new Point2D(first, second);
    }

    size(){
        return this.stack.size;
    }
}

/**
 * Закрашивает весь цвет color цветом paintColor
 * @param {*} ctx 
 * @param {Point2D} p 
 * @param {Array} paintColor
 */
 function zatravka4Color(ctx, p, paintColor, color){
    let stack = new Stack();
    
    let pixel;
    let point = null;
    let count = 0;
    stack.push(p);
    while((stack.size() != 0) && (count <= 250000)){
        pixel = stack.pop();
        
        if (checkPixelColor(ctx, pixel, color)){
            
            setPixel(ctx, pixel, paintColor[0]);
            
            point = new Point2D(pixel.x + 1, pixel.y);
            if (checkPixelColor(ctx, point, color)) {
                stack.push(point);
                count++;
            }
            
            point = new Point2D(pixel.x - 1, pixel.y);
            if (checkPixelColor(ctx, point, color)) {
                stack.push(point);
                count++;
            }

            point = new Point2D(pixel.x, pixel.y + 1);
            if (checkPixelColor(ctx, point, color)) {
                stack.push(point);
                count++
            }

            point = new Point2D(pixel.x, pixel.y - 1);
            if (checkPixelColor(ctx, point, color)) {
                stack.push(point);
                count++;
            }
           
        }
    }
    console.log(count);
}

/**
 * Закрашивает весь цвет color цветом paintColor
 * @param {*} ctx 
 * @param {Point2D} p 
 * @param {Array} paintColor
 */
 function zatravka8Color(ctx, p, paintColor, color){
    let stack = new Stack();
    
    let pixel;
    let point = null;
    let count = 0;
    stack.push(p);
    while((stack.size() != 0) && (count <= 50000)){
        pixel = stack.pop();
         
        if (checkPixelColor(ctx, pixel, color)){
            
            setPixel(ctx, pixel, paintColor[0]);
            
            point = new Point2D(pixel.x + 1, pixel.y);
            if (checkPixelColor(ctx, point, color)) {
                stack.push(point);
                count++;
            }
            
            point = new Point2D(pixel.x - 1, pixel.y);
            if (checkPixelColor(ctx, point, color)) {
                stack.push(point);
                count++;
            }

            point = new Point2D(pixel.x, pixel.y + 1);
            if (checkPixelColor(ctx, point, color)) {
                stack.push(point);
                count++
            }

            point = new Point2D(pixel.x, pixel.y - 1);
            if (checkPixelColor(ctx, point, color)) {
                stack.push(point);
                count++;
            }

            point = new Point2D(pixel.x + 1, pixel.y - 1);
            if (checkPixelColor(ctx, point, color)) {
                stack.push(point);
                count++;
            }
            
            point = new Point2D(pixel.x + 1, pixel.y + 1);
            if (checkPixelColor(ctx, point, color)) {
                stack.push(point);
                count++;
            }

            point = new Point2D(pixel.x - 1, pixel.y + 1);
            if (checkPixelColor(ctx, point, color)) {
                stack.push(point);
                count++
            }

            point = new Point2D(pixel.x - 1, pixel.y - 1);
            if (checkPixelColor(ctx, point, color)) {
                stack.push(point);
                count++;
            }
        }
    }
}

const CANVAS_COLOR = 'rgb(255, 255, 255)';
const DRAW_COLOR = 'rgb(0, 250, 250)';

const canvas = document.querySelector('.canvas');
canvas.width = 500;
canvas.height = 500;
const ctx = canvas.getContext('2d');
let colors = [];

window.addEventListener('click', function (e) {
    if (e.ctrlKey){
        colors = [];
        console.log(e.pageX);
        console.log(e.pageY);

        colors.push(DRAW_COLOR);
        setPixel(ctx, new Point2D(e.pageX, e.pageY), "rgb(0, 0, 0)");
        zatravka8Color(ctx, new Point2D(e.pageX, e.pageY), colors, "rgb(0, 0, 0)");
    }
});

let mouse = { x:0, y:0};
let draw = false;
 
canvas.addEventListener("mousedown", function(e){
     
    mouse.x = e.pageX - this.offsetLeft;
    mouse.y = e.pageY - this.offsetTop;
    draw = true;
    ctx.strokeStyle = DRAW_COLOR;
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(mouse.x, mouse.y);
});
canvas.addEventListener("mousemove", function(e){
     
    if(draw==true){
     
        mouse.x = e.pageX - this.offsetLeft;
        mouse.y = e.pageY - this.offsetTop;
        ctx.lineTo(mouse.x, mouse.y);
        ctx.stroke();
    }
});
canvas.addEventListener("mouseup", function(e){
     
    mouse.x = e.pageX - this.offsetLeft;
    mouse.y = e.pageY - this.offsetTop;
    ctx.lineTo(mouse.x, mouse.y);
    ctx.stroke();
    ctx.closePath();
    draw = false;
});


let isMax = false;
function move() {
    var elem = document.getElementById("myBar");
    var width = 1;
    var id = setInterval(frame, 10);
    function frame() {
        if (width >= 100) {
            isMax = true;
        } 
        if (width <= 1) isMax = false;
        if (isMax) width--;
        else width++;
        elem.style.width = width + "%";
    }
}

move();