
const stages = [
{
title:'1. Python',
topics:['Переменные','Функции','Циклы','ООП','Файлы']
},
{
title:'2. Data Analysis',
topics:['NumPy','Pandas','Matplotlib','Очистка данных']
},
{
title:'3. Math',
topics:['Векторы','Матрицы','Вероятность','Статистика']
},
{
title:'4. Machine Learning',
topics:['Регрессия','Классификация','Scikit-learn','Переобучение']
},
{
title:'5. Neural Networks',
topics:['Нейроны','Backpropagation','PyTorch','TensorFlow']
},
{
title:'6. LLM & AI Apps',
topics:['Transformers','Embeddings','RAG','Agents']
}
];

const roadmap = document.getElementById('roadmap');

stages.forEach((stage,i)=>{
 const card=document.createElement('div');
 card.className='stage';

 let html=`<h2>${stage.title}</h2>`;

 stage.topics.forEach((topic,j)=>{
  const id=`${i}-${j}`;
  html+=`<label><input type="checkbox" data-id="${id}"> ${topic}</label>`;
 });

 card.innerHTML=html;
 roadmap.appendChild(card);
});

const checkboxes=document.querySelectorAll('input[type="checkbox"]');

checkboxes.forEach(cb=>{
 const saved=localStorage.getItem(cb.dataset.id);
 if(saved==='true') cb.checked=true;

 cb.addEventListener('change',()=>{
   localStorage.setItem(cb.dataset.id,cb.checked);
   updateProgress();
 });
});

function updateProgress(){
 const total=checkboxes.length;
 let done=0;

 checkboxes.forEach(cb=>{
   if(cb.checked) done++;
 });

 const percent=Math.round(done/total*100);

 document.getElementById('progress-fill').style.width=percent+'%';
 document.getElementById('progress-text').innerText=percent+'% ('+done+'/'+total+')';
}

updateProgress();
