'use strict';
/**
 * 11 laba
 * 
 * python -m http.server
 * localhost:8000
 */



/**
 * Закрасить пиксель
 * 
 * @param {*} ctx 
 * @param {Array} color
 */
function setPixel(ctx, x, y, color){
    let c = "rgb(" + color[0] + ", " + color[1] + ", " + color[2] + ")";
    // console.log(c);
    ctx.fillStyle = c;
    ctx.fillRect( x, y, 1, 1 );
}

/**
 * Закрасить, используя битмап
 * @param {*} ctx 
 * @param {*} b 
 * @param {*} x 
 * @param {*} y 
 */
function fillRectWithBitmap(ctx, b, x, y){

    for (let i = 0; i < b.length; i++){
        for (let j = 0; j < b[0].length; j++){
            setPixel(ctx, x + i, y + j, b[i][j]);
        }
    }
}

/**
 * "Соединяет" два пикселя, смешивая их цвета
 * 
 * @param {Array} a1 - цвет
 * @param {Array} a2 - цвет 
 * @returns {Array}
 */
function mergePixel(a1, a2){

    let r = Math.round((a1[0] + a2[0]) / 2);
    let g = Math.round((a1[1] + a2[1]) / 2);
    let b = Math.round((a1[2] + a2[2]) / 2);
    return [r, g, b];
}

/**
 * Возвращает битмап прямоугльника
 * 
 * @param {*} ctx 
 * @param {*} x 
 * @param {*} y 
 * @param {*} width 
 * @param {*} height 
 * @returns {Array} arr
 */
function getBitmap(ctx, x, y, width, height){

    let arr = new Array();
    for (let i = 0; i < height; i++){
        let a = new Array();
        for (let j = 0; j < width; j++){
            let data = ctx.getImageData(x + i, y + j, 1, 1).data;
            a.push([data[0], data[1], data[2]]);
        }
        arr.push(a);
    }
    return arr;
}

/**
 * "Сливает" два битмапа 
 * 
 * @param {*} b1 - большой битмап 
 * @param {*} b2 - малый битмап
 * @param {*} x - начало координат на большом 
 * @param {*} y - битмапе, которые нужно "сливать"
 * @returns {Array} битмап
 */
function mergeBitmaps(b1, b2, x, y){
    let res = [];
    for (let i = 0; i < b2.length; i++){

        let a = new Array();
        for (let j = 0; j < b2[0].length; j++){
            a.push(0);
        }
        res.push(a);

        for (let j = 0; j < b2[0].length; j++){
            let p = mergePixel(b1[x + i][y + j], b2[i][j]);
            res[i][j] = p;
        }
    }
    return res;
}

const CANVAS_WIDTH = 1500;
const CANVAS_HEIGHT = 800;

const canvas = document.querySelector('.canvas');
canvas.width = CANVAS_WIDTH;
canvas.height = CANVAS_HEIGHT;
const ctx = canvas.getContext('2d');
let bitmap1 = [];
let bitmap2 = [];

let img1 = document.getElementById("photo1");
let img2 = document.getElementById("photo2");

let isImgloaded = false;
img1.onload = function(){
    isImgloaded = true;
}

img2.onload = function() {
    let x = -400;
    let y = -400;
	ctx.drawImage(img2, x, y);
    bitmap1 = getBitmap(ctx, 0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);
    // для передвижения картинки №2
    let xBitmap2 = 100;
    let yBitmap2 = 200;
    if (isImgloaded){
        ctx.drawImage(img1, xBitmap2, yBitmap2);
        bitmap2 = getBitmap(ctx, xBitmap2, yBitmap2, img1.height, img1.width);
    }
    console.log(img1.height);
    console.log(img1.width);
    let mb = mergeBitmaps(bitmap1, bitmap2, xBitmap2, yBitmap2);
    // console.log(mb);
    // ctx.fillStyle = 'rgb(255, 255, 255)';
    // ctx.fillRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);
    fillRectWithBitmap(ctx, mb, xBitmap2, yBitmap2);
}





