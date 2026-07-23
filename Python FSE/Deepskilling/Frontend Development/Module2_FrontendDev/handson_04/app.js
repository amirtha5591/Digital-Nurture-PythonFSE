const loadBtn = document.getElementById("loadBtn");
const retryBtn = document.getElementById("retryBtn");
const grid = document.querySelector(".course-grid");
const loading = document.getElementById("loading");

// Fetch API Function
async function fetchPosts() {

    try {

        loading.textContent = "Loading Courses...";
        retryBtn.style.display = "none";
        grid.innerHTML = "";

        const response = await fetch(
            "https://jsonplaceholder.typicode.com/posts?_limit=5"
        );

        if (!response.ok) {
            throw new Error("Failed to Fetch Courses");
        }

        const posts = await response.json();

        loading.textContent = "";

        // Course names
        const courseNames = [
            "HTML & CSS",
            "JavaScript Basics",
            "React Development",
            "Python Programming",
            "Database Management"
        ];

        // Course descriptions
        const descriptions = [
            "Learn to create and style web pages using HTML and CSS.",
            "Understand JavaScript fundamentals, DOM and Events.",
            "Build modern web applications using React JS.",
            "Learn Python programming from beginner to intermediate level.",
            "Study SQL, MySQL and database management concepts."
        ];

        posts.forEach((post, index) => {

            const card = document.createElement("div");

            card.className = "course-card";

            card.innerHTML = `
                <h3>${courseNames[index]}</h3>
                <p>${descriptions[index]}</p>
            `;

            grid.appendChild(card);

        });

    }

    catch (error) {

        loading.textContent = "❌ Failed to Load Courses";

        retryBtn.style.display = "inline-block";

        console.log(error);

    }

}

// Load Courses Button
loadBtn.addEventListener("click", fetchPosts);

// Retry Button
if (retryBtn) {

    retryBtn.addEventListener("click", () => {

        fetchPosts();

    });

}

// Axios Demo Function
async function fetchUsingAxios() {

    try {

        const response = await axios.get(
            "https://jsonplaceholder.typicode.com/posts?_limit=5"
        );

        console.log(response.data);

    }

    catch (error) {

        console.log(error);

    }

}