

class Point {
    
    constructor(){
        this.x = 0;
        this.y = 0;
    }

    setPoint(x, y){
        this.x = x;
        this.y = y;
    }
}


class Cube{

    /**
     * 
     * @param {int} x 
     * @param {int} y 
     * @param {int} diff - насколько далеко задний квадра от переднего
     * @param {int} length - расстояние от переднего квадрата до заднего
     */
    constructor(x, y, diff, length){
        
        this.arr = [];

        for (let i = 0; i < n; i++){
            arr.push(new Point);
        }

        this.length = length || 40;
        this.diff = diff || 15;
        this.x = x || -20;
        this.y = y || -20;
        arr[0].setPoint(x, y);
        arr[1].setPoint(x, y + length)
        arr[2].setPoint(x + length, y + length);
        arr[3].setPoint(x + length, y);

        let x1 = x + diff;
        let y1 = y - diff;
        arr[4].setPoint(x1, y1);
        arr[5].setPoint(x1, y1 + length)
        arr[6].setPoint(x1 + length, y1 + length);
        arr[7].setPoint(x1 + length, y1);
    }

    turnX(){

    }

    /**
     * 
     * @param {context} ctx - context of canvas 
     */
    draw(ctx){

    }

}