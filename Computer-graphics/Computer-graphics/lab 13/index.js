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


const CANVAS_WIDTH = 1500;
const CANVAS_HEIGHT = 800;

const canvas = document.querySelector('.canvas');
canvas.width = CANVAS_WIDTH;
canvas.height = CANVAS_HEIGHT;
const ctx = canvas.getContext('2d');
let bitmap1 = [];

let img1 = document.getElementById("photo1");

let isImgloaded = false;
img1.onload = function(){
    let x = -400;
    let y = -400;
	ctx.drawImage(img1, x, y);

    // размер битмапа [n x n]
    let n = 100;
    let xBitmap = 0;
    let yBitmap = 0;
    bitmap1 = getBitmap(ctx, xBitmap, yBitmap, n, n);
    let info = getShadeInfo(bitmap1);

    // посчитаем необходимые данные для отображения "относительных" гистограмм в %
    let sumOfPixels = n * n;
    let shadesInProcR = info[0].map(v => {
        return (v / sumOfPixels * 100).toFixed(3);
    });
    let shadesInProcG = info[1].map(v => {
        return (v / sumOfPixels * 100).toFixed(3);
    });
    let shadesInProcB = info[2].map(v => {
        return (v / sumOfPixels * 100).toFixed(3);
    });
    // посчитаем данные для общих гистограмм
    let aver = [];
    for (let i = 0; i < 256; i++){
        let buf = Math.round((info[0][i] + info[1][i] + info[2][i]) / 3);
        aver.push(buf);
    }
    let averInProc = aver.map(v => {
        return (v / sumOfPixels * 100).toFixed(3);
    });
    // зададим подписи и цвет столбцов
    let labels = [];
    let backColor = [];
    for (let i = 0; i < 256; i++){
        labels.push(i);
        let str = "rgba(" + i +", 0, 0, 0.6)";
        backColor.push(str);
    }

    // график оттенков красного ------------------------------------------
    var shadesOfR = document.getElementById("shadesOfR").getContext("2d");
    var densityData = {
        label: 'Shades of red',
        data: info[0],
        backgroundColor: backColor,
    };
       
    var barChart = new Chart(shadesOfR, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [densityData]
        }
    });
    // график оттенков красного в %
    let shadesOfRInProc = document.getElementById("shadesOfRInProc").getContext("2d");
    var densityData = {
        label: 'Shades of red %',
        data: shadesInProcR,
        backgroundColor: backColor,
    };
    var barChart = new Chart(shadesOfRInProc, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [densityData]
        }
    });
    // график оттенков зеленого ------------------------------------------
    backColor = [];
    for (let i = 0; i < 256; i++){
        let str = "rgba(0, " + i + ", 0, 0.6)";
        backColor.push(str);
    }
    var shadesOfG = document.getElementById("shadesOfG").getContext("2d");
    var densityData = {
        label: 'Shades of green',
        data: info[1],
        backgroundColor: backColor,
    };
       
    var barChart = new Chart(shadesOfG, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [densityData]
        }
    });
    // график оттенков зеленого в %
    let shadesOfGInPro = document.getElementById("shadesOfGInPro").getContext("2d");
    var densityData = {
        label: 'Shades of green %',
        data: shadesInProcG,
        backgroundColor: backColor,
    };
    var barChart = new Chart(shadesOfGInPro, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [densityData]
        }
    });
    // график оттенков синего ------------------------------------------
    backColor = [];
    for (let i = 0; i < 256; i++){
        let str = "rgba(0, 0, " + i + ", 0.6)";
        backColor.push(str);
    }
    var shadesOfB = document.getElementById("shadesOfB").getContext("2d");
    var densityData = {
        label: 'Shades of blue',
        data: info[2],
        backgroundColor: backColor,
    };
       
    var barChart = new Chart(shadesOfB, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [densityData]
        }
    });
    // график оттенков синего в %
    let shadesOfBInPro = document.getElementById("shadesOfBInPro").getContext("2d");
    var densityData = {
        label: 'Shades of blue %',
        data: shadesInProcB,
        backgroundColor: backColor,
    };
    var barChart = new Chart(shadesOfBInPro, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [densityData]
        }
    });

    // график всех оттенков ------------------------------------------
    backColor = [];
    let borderColor = [];
    for (let i = 0; i < 256; i++){
        let str = "rgba(" + i +"," + i + ", " + i + ", 0.6)";
        backColor.push(str);
        borderColor.push("rgba(0, 0, 0, 1)");
    }
    var shadesOfAll = document.getElementById("shadesOfAll").getContext("2d");
    var densityData = {
        label: 'Shades of all shades',
        data: aver,
        backgroundColor: backColor,
        borderColor: borderColor,
        borderWidth: 1,
        hoverBorderWidth: 0
    };
       
    var barChart = new Chart(shadesOfAll, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [densityData]
        }
    });
    // график всех оттенков в %
    let shadesOfAllInProc = document.getElementById("shadesOfAllInProc").getContext("2d");
    var densityData = {
        label: 'Shades of all shades %',
        data: averInProc,
        backgroundColor: backColor,
        borderColor: borderColor,
        borderWidth: 1,
        hoverBorderWidth: 0
    };
    var barChart = new Chart(shadesOfAllInProc, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [densityData]
        }
    });
}





