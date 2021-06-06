'use strict';
/**
 * 12 laba
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
 * Собирает информацию оттенков битмапа
 * 
 * @param {bitmap} bitmap 
 * @returns {Array} 
 */
function getShadeInfo(bitmap){

    let r = new Array();
    let g = new Array();
    let b = new Array();
    for (let i = 0; i < 256; i++){
        r.push(0);
        g.push(0);
        b.push(0);
    }
    for (let i = 0; i < bitmap.length; i++){
        for (let j = 0; j < bitmap[0].length; j++){
            r[bitmap[i][j][0]]++;
            g[bitmap[i][j][1]]++;
            b[bitmap[i][j][2]]++;
        }
    }
    return [r, g, b];
}

 /* Функция для получения текущих координат курсора мыши */
 function getXY(obj_event) {
    let x, y;
    if (obj_event) {
        x = obj_event.clientX;
        y = obj_event.clientY;
    }
    return new Array(x, y);
}

/* Функция для измерения ширины окна */
function clientWidth() {
    return document.documentElement.clientWidth == 0 ? document.body.clientWidth : document.documentElement.clientWidth;
}
/* Функция для измерения высоты окна */
function clientHeight() {
    return document.documentElement.clientHeight == 0 ? document.body.clientHeight : document.documentElement.clientHeight;
}
/* При отпускании кнопки мыши отключаем обработку движения курсора мыши */
function clearXY(evt) {
    document.onmousemove = null;
}

function saveWH(obj_event) {
    let target = obj_event.target.parentElement;

    if (target.classList.contains('block')){
        /* Ставим обработку движения мыши для разных браузеров */
        document.onmousemove = resizeBlock.bind(target);
        return false; // Отключаем стандартную обработку нажатия мыши
    }
}

function resizeBlock(obj_event) {
    let point = getXY(obj_event);
    let block = this;

    // let body = document.querySelector(".blocks");
    let arr = block.getBoundingClientRect();
    // console.log(arr.bottom - point[1]);
    let del = arr.y - point[1];
    console.log(del);
    block.style.height = del + "px"; // Устанавливаем новую высоту блока

    /* Если блок выходит за пределы экрана, то устанавливаем максимальные значения для ширины и высоты */
    if (block.offsetLeft + block.clientWidth > clientWidth()) block.style.width = (clientWidth() - block.offsetLeft)  + "px";
    if (block.offsetTop + block.clientHeight > clientHeight()) block.style.height = (clientHeight() - block.offsetTop) + "px";
}

document.onmouseover = function(event) {
    let target = event.target;

    // если у нас есть подсказка...
    let tooltipHtml = target.dataset.tooltip;
    if (!tooltipHtml) return;

    // ...создадим элемент для подсказки

    tooltipElem = document.createElement('div');
    tooltipElem.className = 'tooltip';
    tooltipElem.innerHTML = tooltipHtml;
    document.body.append(tooltipElem);

    // спозиционируем его сверху от аннотируемого элемента (top-center)
    let coords = target.getBoundingClientRect();
    
    let left = coords.left + (target.offsetWidth - tooltipElem.offsetWidth) / 2;
    if (left < 0) left = 0; // не заезжать за левый край окна

    let top = coords.top - tooltipElem.offsetHeight - 5;
    if (top < 0) { // если подсказка не помещается сверху, то отображать её снизу
        top = coords.top + target.offsetHeight + 5;
    }
    
    tooltipElem.style.left = left + 'px';
    tooltipElem.style.top = top + 'px';
};

document.onmouseout = function(e) {

    if (tooltipElem) {
        tooltipElem.remove();
        tooltipElem = null;
    }

};

let tooltipElem;

const CANVAS_WIDTH = 1920;
const CANVAS_HEIGHT = 1080;

const canvas = document.querySelector('.canvas');
canvas.width = CANVAS_WIDTH;
canvas.height = CANVAS_HEIGHT;
const ctx = canvas.getContext('2d');
let bitmap1 = [];

let img1 = document.getElementById("photo1");

img1.onload = function(){

    let x = 0;
    let y = 0;
	ctx.drawImage(img1, x, y);

    // размер битмапа [n x n]
    let n = 100; //CANVAS_HEIGHT;
    let xBitmap = 0;
    let yBitmap = 0;
    bitmap1 = getBitmap(ctx, xBitmap, yBitmap, n, n);
    let info = getShadeInfo(bitmap1);

    // посчитаем данные для общих гистограмм
    let aver = [];
    for (let i = 0; i < 256; i++){
        let buf = Math.round((info[0][i] + info[1][i] + info[2][i]) / 3);
        aver.push(buf);
    }

    // создадим график
    let color = 1; // r - 0 g - 1 b - 2
    let blocks = document.querySelector(".blocks");
    const kefBlock = 4;
    for (let i = 0; i < 256; i++){
        let block = document.createElement('div');
        block.classList.add('block');
        let tip = "количество: " + info[color][i] + "<br>оттенок " + i;
        block.setAttribute("data-tooltip", tip);
        block.style.height = info[color][i] / kefBlock + 'px';

        let blockResize = document.createElement('div');
        blockResize.classList.add('block_resize');
        document.onmouseup = clearXY; // Ставим обработку на отпускание кнопки мыши
        document.onmousedown = saveWH; // Ставим обработку на нажатие кнопки мыши

        block.append(blockResize);
        blocks.append(block);
    }

}





