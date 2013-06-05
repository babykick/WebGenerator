<%inherit file="base.html" />

<%block name="title">
   first page analysis
</%block>
 
 
<%block name="content">
  <div class="post"> 
      <h2><a href="#"> ${articleTitle}</a><br></h2>
      <p> 
           ## <%include file=${includeFile}/>
           ${articleContent}
      </p>
               
  </div>  
 

</%block>


