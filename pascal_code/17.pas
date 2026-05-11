program RecordExample3;

type
  Vector3 = record
    x : real;
    y : real;
    z : real;
  end;

  Transform = record
    position : Vector3;
    rotation : Vector3;
    scale    : Vector3;
  end;

  GameObject = record
    id         : integer;
    name       : string;
    visible    : boolean;
    transform  : Transform;
    tags       : array[1..4] of string;
  end;

var
  player : GameObject;

begin
  player.id := 1;
  player.name := 'Hero';
  player.visible := true;

  player.transform.position.x := 10.0;
  player.transform.position.y := 20.0;
  player.transform.position.z := 5.0;

  player.transform.rotation.x := 0.0;
  player.transform.rotation.y := 90.0;
  player.transform.rotation.z := 0.0;

  player.transform.scale.x := 1.0;
  player.transform.scale.y := 1.0;
  player.transform.scale.z := 1.0;

  player.tags[1] := 'player';
  player.tags[2] := 'human';
  player.tags[3] := 'warrior';
  player.tags[4] := 'active';
end.