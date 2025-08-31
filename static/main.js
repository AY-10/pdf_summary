const dropArea = document.getElementById('drop-area');
const fileElem = document.getElementById('fileElem');
const status = document.getElementById('status');
const result = document.getElementById('result');
const summaryDiv = document.getElementById('summary');
const snippetDiv = document.getElementById('snippet');
const lengthSelect = document.getElementById('length');
const uploadBtn = document.getElementById('uploadBtn');

['dragenter','dragover','dragleave','drop'].forEach(evtName => {
  dropArea.addEventListener(evtName, preventDefaults, false)
});
function preventDefaults(e){ e.preventDefault(); e.stopPropagation(); }

dropArea.addEventListener('drop', handleDrop, false);
fileElem.addEventListener('change', () => { handleFiles(fileElem.files); });
uploadBtn.addEventListener('click', () => { if(fileElem.files.length) handleFiles(fileElem.files); else alert('Please choose a file first.'); });

function handleDrop(e){
  let dt = e.dataTransfer;
  let files = dt.files;
  handleFiles(files);
}

function handleFiles(files){
  const file = files[0];
  if(!file) return;
  // show filename
  status.innerText = "Ready to upload: " + file.name;
  uploadFile(file);
}

async function uploadFile(file){
  status.innerText = "Uploading...";
  const form = new FormData();
  form.append('file', file);
  form.append('length', lengthSelect.value);
  try {
    const res = await fetch('/api/upload', { method:'POST', body: form });
    const data = await res.json();
    if(res.ok){
      status.innerText = "Done";
      result.classList.remove('hidden');
      summaryDiv.innerText = data.summary || 'No summary';
      snippetDiv.innerText = data.text_snippet || '';
    } else {
      status.innerText = 'Error: ' + (data.error || 'unknown');
      result.classList.add('hidden');
    }
  } catch(err){
    status.innerText = 'Upload failed: ' + err.message;
    result.classList.add('hidden');
  }
}
