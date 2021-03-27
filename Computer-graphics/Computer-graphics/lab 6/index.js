'use strict';

function init(){
    const canvas = document.querySelector('.canvas');
    let ctx = canvas.getContext('2d');

    ctx.fillStyle = 'rgba(0, 0, 0, 1)';
    ctx.fillRect(0, 0, canvas.width, canvas.height); // clear canvas

    let cube = new Cube(ctx, 100, 'rgb(0, 0, 139, 1)', 'rgb(255, 0, 0, 1)');
    cube.move(new Point3D(-50,-50,-50));
      
    let centerScreen = new Point2D(canvas.width / 2, canvas.height / 2);
    cube.put(centerScreen);

    let timer = setInterval
    (
        nextFrame, 
        1000 / 60,
        ctx,
        canvas,
        cube,
        centerScreen
    );

  }

function nextFrame(ctx, canvas, cube, cen6terScreen){
    ctx.fillStyle = 'rgba(0, 0, 0, 1)';  
    ctx.fillRect(0, 0, canvas.width, canvas.height);  // clear canvas
    const btnX = document.querySelector('.checkbox1');
    const btnY = document.querySelector('.checkbox2');
    const btnZ = document.querySelector('.checkbox3');
    if (btnX.checked) {
        cube.rotate('x', 0.4);
    }
    if (btnY.checked) {
        cube.rotate('y', 0.6);
    }
    if (btnZ.checked) {
        cube.rotate('z', 0.3);
    }
    ctx.fillStyle = 'rgba(50, 50, 200, 1)';
    ctx.strokeStyle = 'rgba(60, 60, 210, 1)';
    cube.put(centerScreen);
}


init();

