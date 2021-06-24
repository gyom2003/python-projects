

/**
 * @param {Array} argument def type argument
 */

function minMax(argument) {

    var min = Math.min(argument); 
    var max = Math.max(argument); 
    arr.sort(function(x, y){return x - y});
    return [argument[0], argument[argument.length - 1]], 
    [min, max]; 
    
}


function lessThanOrEqualToZero(num) {
	for (let i = 0; i < 1; i++) {
        if (num <= 0) {
            return true; 
        } else {
            if (num > 0) {
                return false;
            }
        }
    }
}

//exemple de classes
class GeneralClass {

	constructor(name, age) {

		this.name = name;
        this.age = age;
	}

	compareAge(other) {
		if (other.age > other.age && Math.sign(other.age) == 1) {
            return `${other.age} is older than me.`
        }
        if (other.age < other.age && Math.sign(other.age) == -1) {
            return `${other.age} is younger than me.`
        }
        if (other.age == other.age && Math.sign(other.age) == 0) {
            return `${other.age} is the same age as me.`
        }	
    }
    
    //créer d'autres méthodes 
    get thegetterofcalArea() {
        return this.calAreaof(); 
    }

    calAreaof() {
        return this.height * this.width; 
    }
}

const p1 = new GeneralClass("Samuel", 24);
const p2 = new GeneralClass("Joel", 36);
const p3 = new GeneralClass("Lily", 24);

p1.compareAge(p2);
p2.compareAge(p1);
p1.compareAge(p3); 


class Rectangle {
    constructor(height, width) {
      this.height = height;
      this.width = width;
    }
    get area() {
      return this.calcArea();
    }
    calcArea() {
      return this.height * this.width;
    }
  }
  
  const square = new Rectangle(10, 10);
  
  console.log(square.area); // somme donne 100


  class PointCalcul {
      constructor(x, y) {
        this.x = x; 
        this.y = y; 
      }

    //calculer distance deux points (a et b)(racine des diff en x et y)
    theDistance(a, b) {
        const distancex =  a.x - b.x; 
        const distancey = a.y - b.y; 

        return Math.hypot(distancex, distancey); 
    }
  }
  const thePoint1 = new PointCalcul(5, 5); 
  const thePoint2 = new PointCalcul(20, 20); 
  console.log(PointCalcul.theDistance(thePoint1, thePoint2)); 
