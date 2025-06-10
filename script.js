const addFn = document.getElementById("task-form");
let taskInput = document.getElementById("task-input");

const taskList = document.getElementById("task-list");
const storage = localStorage;
const tasks = JSON.parse(localStorage.getItem("task")) || [];

function deleteTask(taskId) {
  tasks.filter((index) => index !== taskId);
}

function showList(input) {
  if (input) {
    taskList.classList.remove("hidden");
    taskList.classList.add("block");
    tasks.forEach((task, ind) => {
      const li = document.createElement("li");
      li.className =
        "flex  justify-between  px-4 py-2 hover:bg-gray-300  items-center border-gray-300";

      li.innerHTML = `
<p class="font-bold list-disc ">${task}</p>
<button onClick="deleteTask(${ind})" class=" bg-red-600 rounded px-4 py-2 border hover:text-black hover:bg-white">Delete</button>
`;
      taskList.appendChild(li);
    });
  }
}

addFn.addEventListener("submit", (e) => {
  e.preventDefault();
  const input = taskInput.value.trim();
  console.log(input, "input .....");

  if (input) {
    tasks.push(input);

    localStorage.setItem("tasks", JSON.stringify(tasks));

    console.log(input, "input added to localStorage");
    taskInput = "";
  }
  showList(input);
});
