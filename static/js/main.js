document.addEventListener('DOMContentLoaded', function() {
    const dropZone = document.getElementById('drop-zone');
    const fileInput = document.getElementById('image');
    const uploadForm = document.getElementById('upload-form');
    const submitBtn = document.getElementById('submit-btn');
    const uploadContent = dropZone.querySelector('.upload-content');

    // Drag & Drop functionality
    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        e.stopPropagation();
        dropZone.classList.add('drag-over');
    });

    dropZone.addEventListener('dragleave', (e) => {
        e.preventDefault();
        e.stopPropagation();
        dropZone.classList.remove('drag-over');
    });

    dropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        e.stopPropagation();
        dropZone.classList.remove('drag-over');
        
        const files = e.dataTransfer.files;
        if (files.length) {
            fileInput.files = files;
            showPreview(files[0]);
        }
    });

    // Click to upload
    dropZone.addEventListener('click', () => {
        fileInput.click();
    });

    fileInput.addEventListener('change', (e) => {
        const file = e.target.files[0];
        if (file) {
            showPreview(file);
        }
    });

    function showPreview(file) {
        if (file && file.type.startsWith('image/')) {
            const reader = new FileReader();
            reader.onload = (e) => {
                // Simpan input file
                const fileInputClone = fileInput.cloneNode(true);
                
                // Update konten drop zone
                dropZone.innerHTML = `
                    <div class="preview-container">
                        <img src="${e.target.result}" alt="Preview" style="max-width: 100%; max-height: 200px; border-radius: 8px;">
                        <p>File terpilih: ${file.name}</p>
                        <button type="button" class="change-file-btn">Ganti Gambar</button>
                    </div>
                `;
                
                // Tambahkan kembali input file
                dropZone.appendChild(fileInputClone);
                
                // Update reference ke input file baru
                fileInput = dropZone.querySelector('input[type="file"]');
                
                // Add event listener untuk tombol ganti gambar
                const changeBtn = dropZone.querySelector('.change-file-btn');
                if (changeBtn) {
                    changeBtn.addEventListener('click', (e) => {
                        e.stopPropagation();
                        fileInput.click();
                    });
                }
            };
            reader.readAsDataURL(file);
        }
    }

    // Form submission
    uploadForm.addEventListener('submit', function(e) {
        if (!fileInput.files.length) {
            e.preventDefault();
            alert('Silakan pilih file gambar terlebih dahulu');
            return;
        }

        // Show loading indicator
        document.getElementById('loading').style.display = 'block';
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Menganalisis...';
    });
});
