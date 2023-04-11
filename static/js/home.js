const searchForm = document.querySelector('form');
const searchBar = document.getElementById('search-bar');
const projectContainer = document.getElementById('project-container');

searchForm.addEventListener('submit', (e) => {
  e.preventDefault();
  const searchValue = searchBar.value.toLowerCase();

  fetch('marvel.json')
    .then(response => response.json())
    .then(data => {
      projectContainer.innerHTML = '';
      data.projects.forEach(project => {
        const projectName = project.name.toLowerCase();
        if (projectName.includes(searchValue)) {
          const projectDiv = document.createElement('div');
          projectDiv.classList.add('project');

          const projectImage = document.createElement('img');
          projectImage.src = project.photos[0];
          projectImage.alt = project.name;

          const projectNameElem = document.createElement('h2');
          projectNameElem.textContent = project.name;

          projectDiv.appendChild(projectImage);
          projectDiv.appendChild(projectNameElem);
          projectContainer.appendChild(projectDiv);
        }
      });
    });
});
