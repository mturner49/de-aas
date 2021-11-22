import React from 'react';

export default () => {
  const onDragStart = (event, nodeType) => {
    event.dataTransfer.setData('application/reactflow', nodeType);
    event.dataTransfer.effectAllowed = 'move';
  };

  return (
    <aside>
      <div className="description">You can drag these nodes to the pane on the right.</div>
      <div className="dndnode snow" onDragStart={(event) => onDragStart(event, 'snow')} draggable>
        Snowflake
      </div>
      <div className="dndnode excel" onDragStart={(event) => onDragStart(event, 'excel')} draggable>
        Excel
      </div>
      <div className="dndnode oracle" onDragStart={(event) => onDragStart(event, 'oracle')} draggable>
        Oracle
      </div>
      <div className="dndnode mongo" onDragStart={(event) => onDragStart(event, 'mongo')} draggable>
      MongoDB
      </div>
      <div className="dndnode custom" onDragStart={(event) => onDragStart(event, 'custom')} draggable>
        Custom
      </div>
      <div className="dndnode python" onDragStart={(event) => onDragStart(event, 'python')} draggable>
        Python
      </div>
    </aside>
  );
};