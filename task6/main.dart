import 'package:flame/flame.dart';
import 'package:flame/game.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'bunny_game.dart';
import 'helpers/directions.dart';
import 'helpers/navigation_keys.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();

  final game = BunnyGame();
  runApp(
    MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        body: Stack(
          children: [
            GameWidget(
              game: game,
            ),
             Align(
               alignment: Alignment.bottomRight,
                 child: NavigationKeys(onDirectionChanged: game.onArrowKeyChanged,),
          )
          ]
         
        ),
      ),
    ),
  );
}
