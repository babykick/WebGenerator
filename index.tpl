<%inherit file="base.html" />

<%block name="title">
    ${student.name}: ${student.course}
</%block>
 
<%block name="navlist">
   <ul>
        <li class="page_item"><a href="index.html">Home</a></li>
        <li class="page_item page-item-links"><a href="first.html" title="first">First</a></li>
        <li class="page_item page-item-text"><a href="mailto:youremailaddress" title="email">Jing Tao</a></li>
  </ul>

</%block> 
 
<%block name="content">
  <div class="post"> 
      <h2><a href="#"> ${post.title}</a><br></h2>
      <p> 
           ## <%include file=${includeFile}/>
           ${post.content}
      </p>
               
  </div>  
 

</%block>

<%block name="sidebarinfo">
   <ul>
     <li> Student Name: ${student.name} </li>
   </ul>
 
</%block>


