document.addEventListener('DOMContentLoaded', function () {
	const dropdown = document.getElementById('userDropdown');

	// Fetch usernames from the backend
	fetch('http://localhost:8000/usernames', {
		method: 'GET'
	})
		.then(response => response.json())
		.then(data => {
			console.log(data);
			// Populate the dropdown with usernames
			data.usernames.forEach(user => {
				const option = document.createElement('option');
				option.value = user; // Assuming user has an 'id' property
				option.textContent = user; // Assuming user has a 'username' property
				dropdown.appendChild(option);
			});
		})
		.catch(error => {
			console.error('Error fetching users:', error);
		});

	// Event listener for dropdown change
	dropdown.addEventListener('change', function () {
		const selectedUserName = dropdown.value;
		console.log(selectedUserName);
		fetch(`http://localhost:8000/user_id/${selectedUserName}`, {
			method: 'GET'
		}).then(response => response.json())
			.then(data => {
				const selectedUserId = data.user_id;

				fetch(`http://localhost:8000/user/${selectedUserId}/posts`, {
					method: 'GET'
				})
					.then(response => response.json())
					.then(data => {
						// Display posts on the page
						console.log(data.posts);
						const postsContainer = document.getElementById('posts');
						postsContainer.innerHTML = ''; // Clear previous posts
						data.posts.forEach(post => {
							const postElement = document.createElement('div');
							postElement.textContent = post.title + ': ' + post.content;
							postsContainer.appendChild(postElement);
						});

						fetch(`http://localhost:8000/articles/${selectedUserId}`, {
							method: 'GET'
						})
							.then(response => response.json())
							.then(data => {
								// Display articles on the page
								console.log(data);
								const articlesContainer = document.getElementById('articles')
								articlesContainer.innerHTML = ''; // Clear previous articles
								data.forEach(article => {
									const articleElement = document.createElement('div');
									articleElement.textContent = article.title + ': ' + article.content;
									articlesContainer.appendChild(articleElement);
								});
							})
							.catch(error => {
								console.error('Error fetching articles:', error);
							});
					})
					.catch(error => {
						console.error('Error fetching posts:', error);
					});

				// Fetch articles of the selected user

			})


	});
});
