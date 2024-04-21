import React, { useRef, useEffect } from 'react'

const {tableau} = window;

function TableauEmbed() {
  const ref = useRef(null);
  const url = "http://public.tableau.com/views/RegionalSampleWorkbook/Storms";

  function initViz() {
    new tableau.Viz(ref.current, url);
  }

  useEffect(() =>{
    initViz();
  }, []);

  return (
    // <div>tableau</div>
    <div ref={ref}></div>
  )
}

export default TableauEmbed;