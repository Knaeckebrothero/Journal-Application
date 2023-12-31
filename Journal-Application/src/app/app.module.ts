import { NgModule, isDevMode } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AppComponent } from './app.component';
import { RouterModule, Routes } from '@angular/router';
import { AppRoutingModule } from './app-routing.module';
import { ServiceWorkerModule } from '@angular/service-worker';

// Components
import { ActivitiesComponent } from './activities/activities.component';
import { NavigationBarComponent } from './navbar/navigation-bar.component';
import { HeadBarComponent } from './head-bar/head-bar.component';
import { RateComponent } from './rate/rate.component';
import { CommentComponent } from './comment/comment.component';

// Material imports
import { MatListModule } from '@angular/material/list';
import { MatIconModule } from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';
import { MatSelectModule } from '@angular/material/select';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatAutocompleteModule } from '@angular/material/autocomplete';
import { ReactiveFormsModule } from '@angular/forms';

// Routes
const routes: Routes = [
  { path: 'activities', component: ActivitiesComponent },
  { path: 'rate', component: RateComponent },
  { path: 'comment', component: CommentComponent },
  { path: '', redirectTo: '/activities', pathMatch: 'full' }
];

@NgModule({
  declarations: [
    AppComponent,
    NavigationBarComponent,
    ActivitiesComponent,
    HeadBarComponent,
    RateComponent,
    CommentComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MatListModule,
    MatIconModule,
    MatSelectModule,
    MatFormFieldModule,
    MatAutocompleteModule,
    ReactiveFormsModule,
    MatInputModule,
    RouterModule.forRoot(routes),
    ServiceWorkerModule.register('ngsw-worker.js', {
      enabled: !isDevMode(),
      // Register the ServiceWorker as soon as the application is stable
      // or after 30 seconds (whichever comes first).
      registrationStrategy: 'registerWhenStable:30000'
    }),
    BrowserAnimationsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
