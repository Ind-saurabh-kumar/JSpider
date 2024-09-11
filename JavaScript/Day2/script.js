


let arr=[10,20,30,40,50];


let res = arr.map((ele, idx, arr) => ele+5);

document.write("<h1>map() --> function</h1>");
document.write("result value",res,"<br>");
document.write("Original array", arr);



let arr2=[20,30,10,2,8,78,89]


let res2= arr2.filter((ele, idx, arr) => ele>20);
document.write("<h1>filter() --> function</h1>");
document.write("result value",res2,"<br>");
document.write("Original array", arr2);



document.write("<h1>filter() --> function find the even number</h1>");
let arr3=[45,30,11,2,8,78,89]


let res3= arr3.filter((ele, idx, arr) => {return ele%2==0});

document.write("result value",res3,"<br>");
document.write("Original array", arr3);




document.write("<h1>find() --> function to search the element</h1>");

let arr4=[45,30,11,2,8,78,89]

target=11


let res4= arr4.find((ele, idx, arr) => {
    document.write("<h3>Hello</h3>" )
    return ele==target});

document.write("found value  ---> ",res4,"<br>");
document.write("Original array --->  ", arr4);




let arr5=[1,2,34,67,12,24,23,43,54,6,8,91];

document.write("<h2>original array is --></h2>", arr5);

let incr=arr5.map((ele, idx, arr5)=> ele+3);
document.write("<h4>Elements Incremented by 3  -></h4>", incr);


let odd=arr5.filter((ele, idx, arr5)=> ele%2!=0);
document.write("<h4>Odd elements are availeable --></h4>", odd);


let f=arr5.find((ele, idx, arr5)=> ele==15);

document.write("<h4>15 elements are availeable --></h4>", f);
res=0;
let sum=arr5.map((ele, idx,arr5)=> res+=ele);
document.write("<h4>Sum of all the elements are --></h4>", res);

var k=7
document.write("<br>", "<h3>Rotation of the array</h3>", "<br>", `${k} times <br>`)

document.write(arr, "<br>")


function rotate(arr, k){
        while(k>0){
            last=arr.pop();
            arr.unshift(last);
            k=k-1; 
        }
        return arr
}

document.write(rotate(arr, k));







