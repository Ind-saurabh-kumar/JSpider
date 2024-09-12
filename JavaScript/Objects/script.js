




// let obj={
//     name:'Saurabh Kumar',
//     id:'indsaurabh',
//     salary:1000,
//     address:'Basavangudi'
// }



// document.write(`<h3>UserName:->${obj['id']}</h3>`);
// document.write("<h3>Name</h3>", `<h3>${obj.name}</h3>`);

// document.write(`<h3>Salary:->  ${obj.salary}</h3>`);

// document.write(`<h3>address->  ${obj['address']}</h3>`);


// // update 

// obj.salary=20000;

// document.write(`<h3>updated Salary:->  ${obj.salary}</h3>`);

// // add new property 

// obj.dept="Artificial Intelligence and Machine Learning";


// document.write(`<h3>added Department later :->  ${obj.dept}</h3>`);



// document.write(`<h3>Nested Object </h3>`);


// let stu={
//     name:'Saurabh',
//     roll:123,
//     marks:{
//         computer:98,
//         maths:70,
//         webtech:98,
//         english:87
//     },
//     displayStuData:()=>{

//         document.write(`The Student name is ${stu.name} and his roll no is ${stu.roll}. He secured Total Marks ${stu.totalmarks}`);
//     },
// }

// document.write(`<h3>Name:->  ${stu.name}</h3>`);

// document.write(`<h3>Computer Marks:->  ${stu.marks.computer}</h3>`);

// document.write(`<h3>Web Tech Marks:->  ${stu.marks.webtech}</h3>`);
// stu.totalmarks =(stu.marks.computer + stu.marks.english + stu.marks.maths + stu.marks.webtech);


// document.write(`<h3>Total Marks:->  ${stu.totalmarks}</h3>`);

// document.write("<h2> Data shows using Function </h2>");

// stu.displayStuData()


// let stu2={
//     name:'Saurabh',
//     roll:123,
//     address:'Basavangudi',
// }


// document.write(`<h2>Keys Present in the Objects are ->  ${Object.keys(stu2)} </h2>`);

// let val=Object.values(stu2);

// console.log(val);

// document.write(`<h2>Values Present in the Objects are ->  ${val} </h2>`)


// let enu=Object.entries(stu2);

// console.log(enu);
// document.write(`<h2>Keys and Values Present in the Objects are ->  ${enu} </h2>`)








let user=[
    {userid:1,
        mobile:12345
    },
    {userid:2,
        mobile:12345
    },
    
    {userid:3,
        mobile:12345
    },
    
    {userid:4,
        mobile:12345
    },
    
    {userid:5,
        mobile:125345
    }
    
    
]


let target=1;

let res= user.find((ele)=> ele.userid==target)
console.log(res);
document.write(res.userid);
