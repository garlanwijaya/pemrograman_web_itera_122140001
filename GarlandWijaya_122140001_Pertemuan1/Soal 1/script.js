// Inisialisasi data
let tasks = JSON.parse(localStorage.getItem('tasks')) || [];

// Simpan data ke localStorage
function saveTasks() {
    localStorage.setItem('tasks', JSON.stringify(tasks));
}

// Render daftar tugas
function renderTasks() {
    console.log('Rendering tasks...');
    const list = document.getElementById('taskList');
    list.innerHTML = '';
    
    tasks.forEach((task, index) => {
        console.log(`Rendering task at index ${index}:`, task);
        const li = document.createElement('li');
        li.classList.add('flex', 'items-center', 'my-2');
        
        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.checked = task.completed;
        checkbox.classList.add('mr-2');
        checkbox.addEventListener('change', () => {
            console.log(`Toggling task at index ${index}`);
            toggleTask(index);
        });
        
        const text = document.createElement('span');
        text.textContent = task.text;
        if (task.completed) {
            text.style.textDecoration = 'line-through';
            text.classList.add('line-through', 'px-2', 'py-1', 'rounded-md', 'text-white', 'bg-gray-500');
        } else {
            text.classList.add('px-2', 'py-1', 'rounded-md', 'text-white', 'bg-blue-500');
        }
        
        const deleteBtn = document.createElement('button');
        deleteBtn.textContent = 'Hapus';
        deleteBtn.classList.add('ml-2', 'px-2', 'py-1', 'text-white', 'rounded-md', 'bg-red-500', 'hover:text-gray-200');
        deleteBtn.addEventListener('click', () => {
            console.log(`Deleting task at index ${index}`);
            deleteTask(index);
        });
        
        li.appendChild(checkbox);
        li.appendChild(text);
        li.appendChild(deleteBtn);
        list.appendChild(li);
    });
    console.log('Finished rendering tasks.');
}

// Tambah tugas baru
document.getElementById('taskForm').addEventListener('submit', (e) => {
    e.preventDefault();
    const input = document.getElementById('taskInput');
    const newText = input.value.trim();
    
    if (newText) {
        tasks.push({text: newText, completed: false});
        saveTasks();
        renderTasks();
        input.value = '';
    }
});

// Toggle status selesai
async function toggleTask(index) {
    console.log(`Attempting to toggle task at index ${index}`);
    tasks[index].completed = !tasks[index].completed;
    console.log(`Task at index ${index} toggled successfully`);
    await saveTasks();
    console.log('Tasks saved successfully');
    await renderTasks();
    console.log('Tasks rendered successfully');
}

// Hapus tugas
async function deleteTask(index) {
    try {
        console.log(`Attempting to delete task at index ${index}`);
        tasks.splice(index, 1);
        console.log('Task deleted successfully');
        await saveTasks();
        console.log('Tasks saved successfully');
        await renderTasks();
        console.log('Tasks rendered successfully');
    } catch (error) {
        console.error('Error deleting task:', error);
    }
}

// Render awal saat halaman dimuat
renderTasks();