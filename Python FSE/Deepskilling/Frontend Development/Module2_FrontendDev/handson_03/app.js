import { courses } from "./data.js";

const grid = document.querySelector(".course-grid");

const totalCredits = document.getElementById("total-credits");

const selectedCourse = document.getElementById("selected-course");

const search = document.getElementById("search-courses");

const sortBtn = document.getElementById("sort-btn");

let courseList = [...courses];
courseList.forEach(course=>{

const {name,credits}=course;

console.log(`${name} (${credits} credits)`);

});

const fourCreditCourses=courseList.filter(course=>course.credits>=4);

console.log(fourCreditCourses);

const total=courseList.reduce((sum,course)=>sum+course.credits,0);

console.log(total);
function renderCourses(courseArray) {

    grid.innerHTML = "";

    courseArray.forEach(course => {

        const card = document.createElement("article");

        card.className = "course-card";

        card.innerHTML = `
            <h3>${course.name}</h3>
            <p>Code: ${course.code}</p>
            <p>Credits: ${course.credits}</p>
            <p>Grade: ${course.grade}</p>
        `;
        card.addEventListener("click", () => {

    selectedCourse.textContent =
        `Selected Course: ${course.name} | Grade: ${course.grade}`;

});

        grid.appendChild(card);

    });

    const total = courseArray.reduce((sum, course) => sum + course.credits, 0);

    totalCredits.textContent = `Total Credits: ${total}`;

}
renderCourses(courseList);
search.addEventListener("input", () => {

    const text = search.value.toLowerCase();

    const filteredCourses = courseList.filter(course =>
        course.name.toLowerCase().includes(text)
    );

    renderCourses(filteredCourses);

});
sortBtn.addEventListener("click", () => {

    courseList.sort((a, b) => b.credits - a.credits);

    renderCourses(courseList);

});